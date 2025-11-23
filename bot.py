import os
import discord
from discord import app_commands
from discord.ext import commands
import asyncio
import random
import re
from typing import Optional

# -------------------------
# CONFIG
# -------------------------
BT = os.getenv("BT")

# -------------------------
# Allowed Roles + Thumbnails
# -------------------------
CDN = "https://cdn.discordapp.com/emojis/"


def emoji_url(emoji_id: int):
    return f"{CDN}/{emoji_id}.png?size=96&quality=lossless"


ALLOWED_ITEM_ROLES = {
    1440783102711562260: "Animals",
    1440778289986670746: "Ancient Terror",
    1441791781636280351: "Burning Blade",
    1441793472008032310: "Crested Queen",
    1441792913813143686: "Devil's Roar Cargo",
    1441792545746321570: "Emissary Flags",
    1441791800900714648: "Feared Redmaw",
    1441793455054651565: "Hungering One",
    1441792052063895602: "Kingly Treasure",
    1441793383776387213: "Servants of the Flame",
}

ROLE_EMOJI_MAP = {
    1440783102711562260: emoji_url(1440781781342093423),
    1440778289986670746: emoji_url(1440782784191926344),
    1441791781636280351: emoji_url(1441902687976427690),
    1441793472008032310: emoji_url(1441902764711088179),
    1441792913813143686: emoji_url(1441902739306053654),
    1441792545746321570: emoji_url(1441902717332099232),
    1441791800900714648: emoji_url(1441902709472231444),
    1441793455054651565: emoji_url(1441902756729323723),
    1441792052063895602: emoji_url(1441902725347541103),
    1441793383776387213: emoji_url(1441902748147908689),
}

# -------------------------
# Bot Setup
# -------------------------
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="!", intents=intents)


# -------------------------
# Offer View
# -------------------------
class OfferView(discord.ui.View):

    def __init__(self, spots: int, duration_seconds: int, creator: discord.Member):
        super().__init__(timeout=None)
        self.creator = creator
        self.spots = spots
        self.duration_seconds = duration_seconds
        self.entrants = []
        self.message = None
        self.embed = None
        self.original_ping = None

    @discord.ui.button(label="Join", style=discord.ButtonStyle.success)
    async def join_button(self, interaction, button):
        if interaction.user in self.entrants:
            return await interaction.response.send_message(
                "You already joined.", ephemeral=True
            )

        self.entrants.append(interaction.user)
        await self.update_embed()
        await interaction.response.send_message("You joined the offer!", ephemeral=True)

    @discord.ui.button(label="Leave", style=discord.ButtonStyle.danger)
    async def leave_button(self, interaction, button):
        if interaction.user not in self.entrants:
            return await interaction.response.send_message(
                "You are not entered.", ephemeral=True
            )

        self.entrants.remove(interaction.user)
        await self.update_embed()
        await interaction.response.send_message("You left the offer!", ephemeral=True)

    async def update_embed(self):
        # Update Entrants field
        for i, field in enumerate(self.embed.fields):
            if field.name == "**Entrants**":
                self.embed.set_field_at(
                    i, name="**Entrants**", value=str(len(self.entrants)), inline=True
                )
                break

        try:
            await self.message.edit(embed=self.embed, view=self)
        except:
            pass


# -------------------------
# Slash Command: /offer
# -------------------------
@bot.tree.command(name="offer", description="Create an item offer")
@app_commands.describe(
    item="Item name (supports @ roles)",
    spots="Number of winners",
    duration="Duration in minutes",
    description="Optional description"
)
async def offer_cmd(interaction: discord.Interaction,
                    item: str,
                    spots: int,
                    duration: int,
                    description: Optional[str] = None):

    await interaction.response.defer(ephemeral=True)

    guild = interaction.guild
    channel = interaction.channel

    if spots <= 0 or duration <= 0:
        return await interaction.followup.send("Spots and Duration must be positive.", ephemeral=True)

    # Extract @roles
    found_role_ids = re.findall(r"<@&(\d+)>", item)
    valid_roles = []
    invalid_roles = []

    for rid in found_role_ids:
        rid = int(rid)
        if rid in ALLOWED_ITEM_ROLES:
            role = guild.get_role(rid)
            if role:
                valid_roles.append(role)
        else:
            invalid_roles.append(rid)

    if invalid_roles:
        return await interaction.followup.send("❌ You mentioned a role that is not allowed.", ephemeral=True)

    header_line = f"# {item}"
    full_description = header_line
    if description:
        full_description += f"\n{description}"

    thumbnail_url = ROLE_EMOJI_MAP.get(valid_roles[0].id) if valid_roles else None
    ping_text = " ".join(role.mention for role in valid_roles) if valid_roles else ""

    embed_color = valid_roles[0].color if valid_roles else discord.Color.blue()
    embed = discord.Embed(description=full_description, color=embed_color)
    embed.add_field(name="**Spots**", value=str(spots), inline=True)
    embed.add_field(name="**Entrants**", value="0", inline=True)

    if thumbnail_url:
        embed.set_thumbnail(url=thumbnail_url)

    embed.set_footer(text=f"Ends in {duration}m 0s • Posted by {interaction.user.display_name}")

    view = OfferView(spots=spots, duration_seconds=duration * 60, creator=interaction.user)

    msg = await channel.send(content=ping_text, embed=embed, view=view)

    view.message = msg
    view.embed = embed
    view.original_ping = ping_text

    # -------------------------
    # Countdown
    # -------------------------
    async def countdown_task():
        remaining = duration * 60

        while remaining > 0:
            mins, secs = divmod(remaining, 60)
            embed.set_footer(text=f"Ends in {mins}m {secs}s • Posted by {interaction.user.display_name}")

            try:
                await msg.edit(embed=embed)
            except:
                pass

            await asyncio.sleep(1)
            remaining -= 1

        # Disable buttons
        for child in view.children:
            child.disabled = True

        embed.set_footer(text=f"Offer Expired • Posted by {interaction.user.display_name}")

        try:
            await msg.edit(content=f"~~{view.original_ping}~~", embed=embed, view=view)
        except:
            pass

        # -------------------------
        # FIX: No entrants
        # -------------------------
        if not view.entrants:
            return await msg.reply(
                "No Entrants - no winner for this offer.\n"
            )

        # Pick winners
        winners = random.sample(view.entrants, min(view.spots, len(view.entrants)))
        winner_lines = "\n".join(f"- {w.mention}" for w in winners)

        announcement = (
            f"{view.creator.mention}\n"
            "__**Winner(s):**__\n"
            f"{winner_lines}\n"
            "-# Please respond to this message with your Xbox gamertag!"
        )

        await msg.reply(announcement)

        # Edit main post with first winner
        first_winner = winners[0].mention
        try:
            await msg.edit(
                content=f"~~{view.original_ping}~~ — Winner: {first_winner}",
                embed=embed,
                view=view
            )
        except:
            pass

    asyncio.create_task(countdown_task())

    await interaction.followup.send("Offer posted!", ephemeral=True)


# -------------------------
# On Ready
# -------------------------
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} ({bot.user.id})")
    try:
        await bot.tree.sync()
        print("Slash commands synced.")
    except Exception as e:
        print("Command sync failed:", e)


# -------------------------
# Enforce Profile Display Role Requirements
# -------------------------

DISPLAY_ROLE_REQUIREMENTS = {
    # display_role_id : required_completion_role_id
    1441788856432197743: 1442181787299352737, # Legendary Completionist -> [P] Legendary Completionist
    1441788904641659032: 1442182442977857537, # Cosmetic Collector -> Cosmetic Completionist
    1441788935050104953: 1442183201865859163, # Notorious Namer -> Social Completionist
    1442176819871612938: 1442182284198285542, # Heckled Host -> Creator Crew Completionist
    1441788963923824797: 1441790535374344222, # Insider Inspector -> Insider Completionist
}

@bot.event
async def on_member_update(before: discord.Member, after: discord.Member):

    # Detect newly added roles
    new_roles = [r for r in after.roles if r not in before.roles]

    if not new_roles:
        return

    for role in new_roles:
        # If the added role is not a display role we care about, ignore it
        if role.id not in DISPLAY_ROLE_REQUIREMENTS:
            continue

        # User ALREADY qualifies? Good.
        if required_role in after.roles:
            return  # do nothing, valid choice

        # User does NOT qualify → remove the role
        try:
            await after.remove_roles(role, reason="User not eligible for display role")
        except:
            pass

        # DM them explaining what happened
        try:
            await after.send(
                f"You selected **{role.name}**, but you do not have the required role.\n"
                "Once you earn it, you'll be able to display this on your profile."
            )
        except:
            pass

# -------------------------
# ROLE GRANT ANNOUNCEMENTS
# -------------------------

COMPLETIONIST_ROLE_IDS = {
    1442181787299352737, # [P] Legendary Completionist
    1442182442977857537, # Cosmetic Completionist
    1442183201865859163, # Social Completionist
    1442182284198285542, # Creator Crew Completionist
    1441790535374344222, # Insider Completionist
}

COMPLETIONIST_THREAD_ID = 1442185694767349812   # Your thread ID
CHANNELS_ROLES_LINK = "https://discord.com/channels/1440700385525239950/customize-community"  # Onboarding Channels & Roles link
DEFAULT_IMAGE_URL = "https://example.com/completionist.png"  # Default image

@bot.event
async def on_member_update(before: discord.Member, after: discord.Member):
    """Detect when a Completionist role is ADDED to a user."""

    # Detect newly added roles
    new_roles = [r for r in after.roles if r not in before.roles]
    if not new_roles:
        return

    # Look for completionist roles
    granted_roles = [r for r in new_roles if r.id in COMPLETIONIST_ROLE_IDS]
    if not granted_roles:
        return

    role = granted_roles[0]

    # Fetch thread
    thread = after.guild.get_thread(COMPLETIONIST_THREAD_ID)
    if thread is None:
        print("❌ Completionist thread not found!")
        return

    # Count how many members have this role
    fellow_count = sum(1 for member in after.guild.members if role in member.roles)

    # Embed (without mentioning the user)
    embed = discord.Embed(
        title="🏆 Completionist Unlocked!",
        description=f"# {role.name}",  # Only the role in # format
        color=role.color
    )

    # Two-column fields
    embed.add_field(
        name="**To Customise Your Profile:**",
        value=f"[Open Onboarding]({ONBOARDING_LINK}) to choose your channels & roles.",
        inline=True
    )
    embed.add_field(
        name="**Fellow Completionists:**",
        value=f"{fellow_count} members have this role.",
        inline=True
    )

    # Set image at bottom
    embed.set_image(url=getattr(role, "icon", DEFAULT_IMAGE_URL))

    # Send the message, mentioning the user outside the embed
    await thread.send(content=after.mention, embed=embed)

# -------------------------
# Run Bot
# -------------------------
bot.run(BT)








