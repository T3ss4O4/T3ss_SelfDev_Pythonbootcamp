# Given is a list of 5 self.dev members of your choice.
# Create a list of dictionaries with the following keys for each member:
# instagram username, discord name, reason why they want to learn programming.
# Save that dictionary in a file called selfdev_members.json
import json

members = [{
    'name': 'long',
    'discord_name': 'long#0575',
    'reason_to_code': 'he is lazy'
    },
    {
    'name': 'isaac',
    'discord_name': 'pinsaregood#4874',
    'reason_to_code': 'he wants to process videos (or summon demons)'
    },
    {
    'name': 'Ash',
    'discord_name': 'Aakash1103Jha#4684',
    'reason_to_code': 'Invent the next viral social media app.'
    },
    {
    'name': 'Albina',
    'discord_name': 'alb#9489',
    'reason_to_code': 'Take over the World.'
    },
    {
    'name': 'Tess',
    'discord_name': 'Norwija#6914',
    'reason_to_code': 'Get an A+ at university.'
    }
]

o_file = open("selfdev_members.json", "w")

o_file.write(json.dumps(members, indent=4))

o_file.close()
