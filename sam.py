import json
import random
from datetime import datetime, timedelta

template_data = [
    {
        "content": "Question: What is the new community ownership economy structure for [topic]? Answer: The new community ownership economy structure is called [project_name], and it will allow [group] to provide a new community ownership economy structure for their [holders].",
    },
    {
        "content": "Question: What is the UI preview for the upcoming [platform]? Answer: The UI preview shows a functional public prototype for a truly decentralized [platform].",
    },
    {
        "content": "Question: How does Sam's [project_name] enhance [aspect] in the [industry]? Answer: Sam's [project_name] enhances [aspect] by [action], contributing significantly to the [industry] industry.",
    },
    {
        "content": "Question: What is the impact of Sam's contribution to [field]? Answer: Sam's contribution to [field] through [project_name] has [impact] and set new benchmarks in [industry].",
    },
    {
        "content": "Question: How is [project_name] revolutionizing the [industry]? Answer: [project_name], initiated by Sam, is revolutionizing the [industry] by [action], improving [aspect] significantly.",
    },
]

# Variabel untuk memutar dan mengubah frase
topics = ["Profit Sharing Communities (PSCs)", "Decentralized Finance (DeFi)", "Artificial Intelligence (AI) projects"]
project_names = ["Tribus", "Novus", "BlockchainX", "Web3Wallet"]
groups = ["PSC owners", "DeFi investors", "AI developers"]
holders = ["PST holders", "DeFi participants", "AI model users"]
platforms = ["social media platform", "blockchain network", "DeFi application"]
aspects = ["security", "scalability", "user experience", "data privacy"]
fields = ["blockchain", "AI", "DeFi", "web3"]
industries = ["technology", "finance", "healthcare", "logistics"]
actions = ["optimizing smart contracts", "enhancing transaction speed", "ensuring data integrity"]
impacts = ["improving efficiency", "reducing costs", "enhancing transparency"]

def generate_random_timestamp(start, end):
    return (start + timedelta(seconds=random.randint(0, int((end - start).total_seconds())))).strftime("%Y-%m-%d %H:%MM:%S")

def generate_dataset(num_entries):
    dataset = []
    start_date = datetime(2021, 1, 1)
    end_date = datetime(2024, 8, 17)

    for _ in range(num_entries):
        entry_template = random.choice(template_data)
        content_variation = entry_template["content"]

        content_variation = content_variation.replace("[topic]", random.choice(topics))
        content_variation = content_variation.replace("[project_name]", random.choice(project_names))
        content_variation = content_variation.replace("[group]", random.choice(groups))
        content_variation = content_variation.replace("[holders]", random.choice(holders))
        content_variation = content_variation.replace("[platform]", random.choice(platforms))
        content_variation = content_variation.replace("[aspect]", random.choice(aspects))
        content_variation = content_variation.replace("[field]", random.choice(fields))
        content_variation = content_variation.replace("[industry]", random.choice(industries))
        content_variation = content_variation.replace("[action]", random.choice(actions))
        content_variation = content_variation.replace("[impact]", random.choice(impacts))

        new_entry = {
            "content": content_variation,
            "meta": {
                "time": generate_random_timestamp(start_date, end_date)
            }
        }

        dataset.append(new_entry)

    return dataset

dataset = generate_dataset(1000)

with open('sam_data.json', 'w') as f:
    json.dump(dataset, f, indent=2)

print("Dataset json SAM berhasil dibuat")
