#!/usr/bin/env python3
"""
================================================================================
Name: Cbwinslow
Date: 2026-03-20
Script Name: curriculum_repo_list.py
Version: 1.0.0
Log Summary: Generated comprehensive curriculum repository list for AI/ML
Description:
    Generates a formatted curriculum repository list for intermediate/advanced
    TypeScript, Python, and AI/ML programming. Output is optimized for ingestion
    by AI agents (instructor, content generator, etc.) for curriculum development.

Change Summary:
    - Initial creation with curated repositories across three domains
    - Formatted for easy parsing by downstream AI agents
    - Includes metadata for sorting and categorization

Inputs:
    - None (script generates data internally)

Outputs:
    - curriculum_repos.json: Structured repository data
    - curriculum_repos.md: Markdown formatted list
    - curriculum_repos.csv: CSV formatted list for spreadsheet import
================================================================================
"""

import json
import csv
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any


class CurriculumRepository:
    """Represents a learning repository with metadata."""
    
    def __init__(
        self,
        name: str,
        owner: str,
        url: str,
        category: str,
        level: str,
        description: str,
        key_topics: List[str],
        best_for: str,
        stars: int = 0,
        language: str = "Mixed"
    ):
        self.name = name
        self.owner = owner
        self.url = url
        self.category = category
        self.level = level
        self.description = description
        self.key_topics = key_topics
        self.best_for = best_for
        self.stars = stars
        self.language = language

    def to_dict(self) -> Dict[str, Any]:
        """Convert repository to dictionary."""
        return {
            "name": self.name,
            "owner": self.owner,
            "url": self.url,
            "category": self.category,
            "level": self.level,
            "description": self.description,
            "key_topics": self.key_topics,
            "best_for": self.best_for,
            "stars": self.stars,
            "language": self.language
        }


class CurriculumGenerator:
    """Generates curriculum repository lists in multiple formats."""
    
    TYPESCRIPT_REPOS = [
        CurriculumRepository(
            name="advanced-ts",
            owner="hatefrad",
            url="https://github.com/hatefrad/advanced-ts",
            category="TypeScript",
            level="Advanced",
            description="Focused on advanced TypeScript techniques: mapped/conditional/infer/template literal types, type system performance, deep dive utility types, React strict typing, and production patterns.",
            key_topics=["Advanced Types", "Type System", "Design Patterns", "React", "Backend"],
            best_for="Production-grade TypeScript mastery",
            stars=8500,
            language="TypeScript"
        ),
        CurriculumRepository(
            name="type-challenges",
            owner="type-challenges",
            url="https://github.com/type-challenges/type-challenges",
            category="TypeScript",
            level="Advanced",
            description="Hundreds of advanced TypeScript typing challenges to master the type system. Learn to create powerful utility types, mapped/conditional/distributed types.",
            key_topics=["Type Challenges", "Utility Types", "Advanced Types", "Type Inference"],
            best_for="Expert-level type system training",
            stars=44000,
            language="TypeScript"
        ),
        CurriculumRepository(
            name="design-patterns-typescript",
            owner="torokmark",
            url="https://github.com/torokmark/design-patterns-typescript",
            category="TypeScript",
            level="Advanced",
            description="Classic design patterns (creational, structural, behavioral) coded in idiomatic TypeScript with clear implementations and explanations.",
            key_topics=["Design Patterns", "Architecture", "OOP", "Best Practices"],
            best_for="Learning production architecture patterns",
            stars=4200,
            language="TypeScript"
        ),
        CurriculumRepository(
            name="Learn-Typescript",
            owner="pranav89624",
            url="https://github.com/pranav89624/Learn-Typescript",
            category="TypeScript",
            level="Intermediate-Advanced",
            description="Hands-on guide covering core types, advanced patterns, React, and Node.js with practical exercises and progressive difficulty.",
            key_topics=["Core Types", "Advanced Patterns", "React", "Node.js", "Full Stack"],
            best_for="Full stack TypeScript development",
            stars=2800,
            language="TypeScript"
        ),
        CurriculumRepository(
            name="typescript-book",
            owner="gibbok",
            url="https://github.com/gibbok/typescript-book",
            category="TypeScript",
            level="Intermediate-Advanced",
            description="Concise, open-source TypeScript guide covering effective advanced usage patterns and real-world best practices in production.",
            key_topics=["Best Practices", "Production Code", "Advanced Patterns", "Real-World Applications"],
            best_for="Practical TypeScript for production",
            stars=6500,
            language="TypeScript"
        ),
        CurriculumRepository(
            name="developer-roadmap",
            owner="kamranahmedse",
            url="https://github.com/kamranahmedse/developer-roadmap",
            category="TypeScript",
            level="Intermediate-Advanced",
            description="Detailed TypeScript learning roadmap with links to advanced topics, design patterns, and ecosystem libraries.",
            key_topics=["Learning Roadmap", "Architecture", "Design Patterns", "Ecosystem"],
            best_for="Structured TypeScript learning path",
            stars=292000,
            language="Mixed"
        ),
    ]

    PYTHON_REPOS = [
        CurriculumRepository(
            name="Python",
            owner="TheAlgorithms",
            url="https://github.com/TheAlgorithms/Python",
            category="Python",
            level="Intermediate-Advanced",
            description="Comprehensive algorithms and data structures repository. Hundreds of well-organized, readable implementations including searching, sorting, dynamic programming, and graphs.",
            key_topics=["Algorithms", "Data Structures", "Graph Theory", "Dynamic Programming", "Sorting"],
            best_for="Algorithm mastery and technical interviews",
            stars=196000,
            language="Python"
        ),
        CurriculumRepository(
            name="data-structures-and-algorithms-in-python",
            owner="Deepali-Srivastava",
            url="https://github.com/Deepali-Srivastava/data-structures-and-algorithms-in-python",
            category="Python",
            level="Intermediate-Advanced",
            description="Clear code and explanations for data structures and algorithms from basics to advanced topics like trees, graphs, and dynamic programming.",
            key_topics=["Data Structures", "Algorithms", "Trees", "Graphs", "Dynamic Programming"],
            best_for="Step-by-step DSA learning",
            stars=2200,
            language="Python"
        ),
        CurriculumRepository(
            name="Strivers-A2Z-DSA-Sheet",
            owner="striver79",
            url="https://github.com/striver79/Strivers-A2Z-DSA-Sheet",
            category="Python",
            level="Intermediate-Advanced",
            description="Based on Striver's famous DSA roadmap. Huge collection of questions, patterns, and explanations in Python for beginner to advanced levels.",
            key_topics=["DSA Problems", "Patterns", "Interview Prep", "Comprehensive Coverage"],
            best_for="Interview-focused algorithm practice",
            stars=32000,
            language="Python"
        ),
        CurriculumRepository(
            name="Data-Structure-and-Algorithms",
            owner="pkprajapati7402",
            url="https://github.com/pkprajapati7402/Data-Structure-and-Algorithms",
            category="Python",
            level="Intermediate-Advanced",
            description="Well-documented data structures, algorithms, and solutions to popular DSA problems from CodeChef and Love Babbar DSA sheets.",
            key_topics=["DSA", "Competitive Programming", "Problem Solving", "Multi-Language"],
            best_for="Competitive programming preparation",
            stars=1500,
            language="Python"
        ),
        CurriculumRepository(
            name="project-based-learning",
            owner="practical-tutorials",
            url="https://github.com/practical-tutorials/project-based-learning",
            category="Python",
            level="Intermediate-Advanced",
            description="Curated list of project-based tutorials using advanced algorithms and data structures in real-world applications.",
            key_topics=["Project-Based Learning", "Real-World Applications", "Practical Skills"],
            best_for="Applying DSA knowledge to real projects",
            stars=145000,
            language="Mixed"
        ),
    ]

    AIML_REPOS = [
        CurriculumRepository(
            name="tensorflow",
            owner="tensorflow",
            url="https://github.com/tensorflow/tensorflow",
            category="AI/ML",
            level="Advanced",
            description="Official TensorFlow repository with comprehensive tutorials, models, and the full TensorFlow ecosystem for deep learning.",
            key_topics=["Deep Learning", "Neural Networks", "TensorFlow Ecosystem", "Production ML"],
            best_for="Advanced deep learning and production deployment",
            stars=185000,
            language="Python"
        ),
        CurriculumRepository(
            name="pytorch",
            owner="pytorch",
            url="https://github.com/pytorch/pytorch",
            category="AI/ML",
            level="Advanced",
            description="Leading deep learning research framework with excellent documentation and sample code for custom model development.",
            key_topics=["Deep Learning", "Neural Networks", "PyTorch", "Research"],
            best_for="Advanced deep learning research and custom models",
            stars=84000,
            language="Python"
        ),
        CurriculumRepository(
            name="transformers",
            owner="huggingface",
            url="https://github.com/huggingface/transformers",
            category="AI/ML",
            level="Advanced",
            description="State-of-the-art models for NLP and beyond. Provides pre-trained models, fine-tuning capabilities, and extensive documentation.",
            key_topics=["NLP", "Transformers", "Pre-trained Models", "Transfer Learning"],
            best_for="Advanced NLP and transformer-based models",
            stars=135000,
            language="Python"
        ),
        CurriculumRepository(
            name="fastai",
            owner="fastai",
            url="https://github.com/fastai/fastai",
            category="AI/ML",
            level="Intermediate-Advanced",
            description="High-level deep learning library on top of PyTorch. Excellent for building advanced models with minimal code.",
            key_topics=["Deep Learning", "Computer Vision", "NLP", "Transfer Learning"],
            best_for="Rapid deep learning model development",
            stars=26000,
            language="Python"
        ),
        CurriculumRepository(
            name="scikit-learn",
            owner="scikit-learn",
            url="https://github.com/scikit-learn/scikit-learn",
            category="AI/ML",
            level="Intermediate",
            description="Robust machine learning library in Python. Good for transitioning from classical ML to deeper models with production-quality code.",
            key_topics=["Machine Learning", "Classification", "Regression", "Clustering"],
            best_for="Classical ML and scikit-learn best practices",
            stars=60000,
            language="Python"
        ),
        CurriculumRepository(
            name="spinningup",
            owner="openai",
            url="https://github.com/openai/spinningup",
            category="AI/ML",
            level="Advanced",
            description="OpenAI's educational resource for deep reinforcement learning, including theory and practical coding exercises.",
            key_topics=["Reinforcement Learning", "Deep RL", "Policy Gradient", "Q-Learning"],
            best_for="Mastering deep reinforcement learning",
            stars=10000,
            language="Python"
        ),
        CurriculumRepository(
            name="annotated_deep_learning_paper_implementations",
            owner="labmlai",
            url="https://github.com/labmlai/annotated_deep_learning_paper_implementations",
            category="AI/ML",
            level="Advanced",
            description="Code implementations of cutting-edge deep learning research papers with detailed annotations for understanding.",
            key_topics=["Deep Learning Research", "Advanced Techniques", "Paper Implementations", "Annotated Code"],
            best_for="Understanding latest ML research",
            stars=21000,
            language="Python"
        ),
        CurriculumRepository(
            name="homemade-machine-learning",
            owner="trekhleb",
            url="https://github.com/trekhleb/homemade-machine-learning",
            category="AI/ML",
            level="Intermediate",
            description="Build ML algorithms from scratch to deepen understanding of how they work internally.",
            key_topics=["ML from Scratch", "Algorithm Understanding", "Educational"],
            best_for="Deep understanding of ML fundamentals",
            stars=24000,
            language="Python"
        ),
        CurriculumRepository(
            name="awesome-machine-learning",
            owner="josephmisiti",
            url="https://github.com/josephmisiti/awesome-machine-learning",
            category="AI/ML",
            level="Intermediate-Advanced",
            description="Curated list of ML libraries, frameworks, tools, and resources categorized by language and application.",
            key_topics=["ML Tools", "Libraries", "Frameworks", "Resources"],
            best_for="ML stack selection and ecosystem overview",
            stars=65000,
            language="Mixed"
        ),
        CurriculumRepository(
            name="awesome-deep-learning",
            owner="ChristosChristofidis",
            url="https://github.com/ChristosChristofidis/awesome-deep-learning",
            category="AI/ML",
            level="Advanced",
            description="Comprehensive collection of deep learning frameworks, tutorials, books, and cutting-edge research.",
            key_topics=["Deep Learning", "Frameworks", "Research", "Learning Resources"],
            best_for="Comprehensive deep learning resource guide",
            stars=22000,
            language="Mixed"
        ),
    ]

    def __init__(self):
        """Initialize the curriculum generator."""
        self.all_repos = self.TYPESCRIPT_REPOS + self.PYTHON_REPOS + self.AIML_REPOS
        self.output_dir = Path(".")

    def generate_json(self, filename: str = "curriculum_repos.json") -> None:
        """Generate JSON output file."""
        data = {
            "metadata": {
                "generated_at": datetime.now().isoformat(),
                "total_repositories": len(self.all_repos),
                "categories": {
                    "TypeScript": len(self.TYPESCRIPT_REPOS),
                    "Python": len(self.PYTHON_REPOS),
                    "AI/ML": len(self.AIML_REPOS)
                }
            },
            "repositories": [repo.to_dict() for repo in self.all_repos]
        }
        
        with open(self.output_dir / filename, 'w') as f:
            json.dump(data, f, indent=2)
        
        print(f"✓ Generated {filename}")

    def generate_markdown(self, filename: str = "curriculum_repos.md") -> None:
        """Generate Markdown formatted output."""
        lines = [
            "# Intermediate/Advanced Programming Curriculum - Repository List\n",
            f"*Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*\n\n",
            f"**Total Repositories: {len(self.all_repos)}**\n\n",
            "This curated list contains the best repositories for learning intermediate to advanced ",
            "TypeScript, Python, and AI/ML programming. Designed for use with AI curriculum agents.\n\n",
            "---\n\n"
        ]

        # TypeScript Section
        lines.append("## TypeScript (6 Repositories)\n\n")
        for i, repo in enumerate(self.TYPESCRIPT_REPOS, 1):
            lines.append(self._format_md_repo_entry(i, repo))

        # Python Section
        lines.append("\n## Python (5 Repositories)\n\n")
        for i, repo in enumerate(self.PYTHON_REPOS, 1):
            lines.append(self._format_md_repo_entry(i, repo))

        # AI/ML Section
        lines.append("\n## AI/ML (10 Repositories)\n\n")
        for i, repo in enumerate(self.AIML_REPOS, 1):
            lines.append(self._format_md_repo_entry(i, repo))

        with open(self.output_dir / filename, 'w') as f:
            f.writelines(lines)
        
        print(f"✓ Generated {filename}")

    def _format_md_repo_entry(self, index: int, repo: CurriculumRepository) -> str:
        """Format a repository entry for Markdown."""
        topics = ", ".join(repo.key_topics)
        return (
            f"### {index}. {repo.name}\n\n"
            f"**Owner:** {repo.owner}  \n"
            f"**URL:** {repo.url}  \n"
            f"**Level:** {repo.level} | **Language:** {repo.language}  \n"
            f"**Stars:** ⭐ {repo.stars:,}\n\n"
            f"**Description:**  \n{repo.description}\n\n"
            f"**Key Topics:** {topics}\n\n"
            f"**Best For:** {repo.best_for}\n\n"
            f"---\n\n"
        )

    def generate_csv(self, filename: str = "curriculum_repos.csv") -> None:
        """Generate CSV formatted output."""
        fieldnames = [
            "Index", "Name", "Owner", "URL", "Category", "Level", 
            "Language", "Stars", "Description", "Key Topics", "Best For"
        ]
        
        with open(self.output_dir / filename, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            
            for idx, repo in enumerate(self.all_repos, 1):
                writer.writerow({
                    "Index": idx,
                    "Name": repo.name,
                    "Owner": repo.owner,
                    "URL": repo.url,
                    "Category": repo.category,
                    "Level": repo.level,
                    "Language": repo.language,
                    "Stars": repo.stars,
                    "Description": repo.description,
                    "Key Topics": "; ".join(repo.key_topics),
                    "Best For": repo.best_for
                })
        
        print(f"✓ Generated {filename}")

    def generate_all(self) -> None:
        """Generate all output formats."""
        print("\n" + "="*70)
        print("Curriculum Repository List Generator")
        print("="*70 + "\n")
        
        self.generate_json()
        self.generate_markdown()
        self.generate_csv()
        
        print("\n" + "="*70)
        print(f"Successfully generated curriculum lists with {len(self.all_repos)} repositories")
        print("="*70 + "\n")
        print("Output files:")
        print("  • curriculum_repos.json  (JSON format for API/agent consumption)")
        print("  • curriculum_repos.md    (Markdown for documentation)")
        print("  • curriculum_repos.csv   (CSV for spreadsheet import)")
        print("\n")


def main():
    """Main execution function."""
    generator = CurriculumGenerator()
    generator.generate_all()


if __name__ == "__main__":
    main()