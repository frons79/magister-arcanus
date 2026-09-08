from __future__ import annotations

import discord

DEMIURGE_ROLE_NAME = "Demiurgo"


async def get_demiurge_role(guild: discord.Guild) -> discord.Role | None:
    """Return the server's Demiurgo role, if it exists."""
    return discord.utils.get(guild.roles, name=DEMIURGE_ROLE_NAME)


async def ensure_demiurge_role(guild: discord.Guild) -> discord.Role:
    """Create the Demiurgo role when necessary."""
    role = await get_demiurge_role(guild)
    if role is not None:
        return role
    return await guild.create_role(
        name=DEMIURGE_ROLE_NAME,
        mentionable=False,
        reason="Magister Arcanus: create the unique Demiurgo permission",
    )


async def is_demiurge(member: discord.Member) -> bool:
    role = await get_demiurge_role(member.guild)
    return role is not None and role in member.roles


async def appoint_demiurge(
    guild: discord.Guild, target: discord.Member
) -> discord.Role:
    """Transfer the unique Demiurgo permission to exactly one member."""
    role = await ensure_demiurge_role(guild)

    for current in tuple(role.members):
        if current.id != target.id:
            await current.remove_roles(
                role,
                reason="Magister Arcanus: transfer unique Demiurgo permission",
            )

    if role not in target.roles:
        await target.add_roles(
            role,
            reason="Magister Arcanus: appoint Demiurgo",
        )
    return role


async def remove_demiurge(guild: discord.Guild) -> None:
    """Remove the Demiurgo permission from every member."""
    role = await get_demiurge_role(guild)
    if role is None:
        return
    for member in tuple(role.members):
        await member.remove_roles(
            role,
            reason="Magister Arcanus: revoke Demiurgo permission",
        )


def can_bootstrap_demiurge(member: discord.Member) -> bool:
    """Only a server administrator may appoint the first Demiurgo."""
    return member.guild_permissions.administrator
