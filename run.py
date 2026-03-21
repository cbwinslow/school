#!/usr/bin/env python3
"""
================================================================================
Name: Cbwinslow
Date: 2026-03-20
Script Name: run.py
Version: 1.0.0
Description:
    Main entry point for the AI-Powered Curriculum Generator.
    Provides both TUI (Terminal User Interface) and Web interface options.
    Orchestrates agent workflows for curriculum generation.

Inputs:
    - Command line arguments (optional)
    - User input via TUI/Web

Outputs:
    - Generated curriculum files (JSON, Markdown, CSV)
    - Console output with progress
================================================================================
"""

import sys
import json
import argparse
from pathlib import Path
from typing import Optional, Dict, Any
from datetime import datetime

# Import existing scripts
try:
    from curriculum_repo_list import CurriculumGenerator
    from github_repo_to_curriculum_generator import (
        GitHubRepoAnalyzer,
        CurriculumFromRepoGenerator
    )
    from recursive_curriculum_generator import ContentGenerator
except ImportError as e:
    print(f"Error importing modules: {e}")
    print("Make sure all Python scripts are in the same directory.")
    sys.exit(1)


class CurriculumRunner:
    """Main runner for curriculum generation with TUI interface."""

    def __init__(self):
        """Initialize the curriculum runner."""
        self.output_dir = Path("output")
        self.output_dir.mkdir(exist_ok=True)
        self.github_token = None

    def print_banner(self):
        """Print welcome banner."""
        print("\n" + "=" * 70)
        print("   AI-POWERED CURRICULUM GENERATOR")
        print("=" * 70)
        print("   Generate complete learning curricula from:")
        print("   • GitHub repositories")
        print("   • Predefined outlines")
        print("   • Topic specifications")
        print("=" * 70 + "\n")

    def print_menu(self):
        """Print main menu."""
        print("\n📋 MAIN MENU")
        print("-" * 40)
        print("1. Generate curriculum from GitHub repo")
        print("2. Generate curriculum from outline file")
        print("3. Generate curriculum by topic")
        print("4. List available repositories")
        print("5. View agent skills")
        print("6. Settings")
        print("0. Exit")
        print("-" * 40)

    def get_user_choice(self, prompt: str = "Enter choice: ") -> str:
        """Get user input."""
        try:
            return input(prompt).strip()
        except (EOFError, KeyboardInterrupt):
            print("\n\nGoodbye!")
            sys.exit(0)

    def generate_from_github(self):
        """Generate curriculum from a GitHub repository."""
        print("\n📚 Generate Curriculum from GitHub Repository")
        print("-" * 50)

        # Get repository info
        repo_input = self.get_user_choice("Enter repository (owner/name): ")

        if "/" not in repo_input:
            print("❌ Invalid format. Use: owner/repo_name")
            return

        owner, repo_name = repo_input.split("/", 1)

        # Get target audience
        print("\nTarget audience level:")
        print("1. Beginner")
        print("2. Intermediate")
        print("3. Advanced")
        level_choice = self.get_user_choice("Choose level (1-3): ")

        levels = {"1": "beginner", "2": "intermediate", "3": "advanced"}
        target_audience = levels.get(level_choice, "intermediate")

        print(f"\n⏳ Analyzing repository: {owner}/{repo_name}...")

        try:
            # Step 1: Analyze repository
            analyzer = GitHubRepoAnalyzer(token=self.github_token)
            repo_analysis = analyzer.analyze_repository(owner, repo_name)

            print(f"✓ Found {len(repo_analysis.main_concepts)} concepts")
            print(f"✓ Language: {repo_analysis.language}")
            print(f"✓ Key files: {len(repo_analysis.key_files)}")

            # Step 2: Generate curriculum
            print("\n⏳ Generating curriculum...")
            generator = CurriculumFromRepoGenerator(repo_analysis)
            curriculum = generator.generate_curriculum()

            # Step 3: Save outputs
            output_file = self.output_dir / f"{repo_name}_curriculum.json"
            with open(output_file, 'w') as f:
                json.dump(curriculum, f, indent=2)

            print(f"\n✅ Curriculum generated successfully!")
            print(f"📁 Output: {output_file}")

            # Show summary
            self._print_curriculum_summary(curriculum)

        except Exception as e:
            print(f"\n❌ Error: {str(e)}")
            print("Make sure the repository exists and is accessible.")

    def generate_from_outline(self):
        """Generate curriculum from an outline file."""
        print("\n📚 Generate Curriculum from Outline")
        print("-" * 50)

        outline_file = self.get_user_choice("Enter outline file path: ")

        outline_path = Path(outline_file)
        if not outline_path.exists():
            print(f"❌ File not found: {outline_file}")
            return

        try:
            with open(outline_path, 'r') as f:
                outline = json.load(f)

            print(f"✓ Loaded outline: {outline.get('course_name', 'Unknown')}")

            # Get domain
            print("\nSelect domain:")
            print("1. Python")
            print("2. TypeScript")
            print("3. AI/ML")
            domain_choice = self.get_user_choice("Choose domain (1-3): ")

            domains = {"1": "python", "2": "typescript", "3": "aiml"}
            domain = domains.get(domain_choice, "python")

            print(f"\n⏳ Generating {domain} curriculum...")

            # Generate curriculum
            generator = ContentGenerator(domain=domain)
            curriculum = generator.generate_curriculum_recursive(outline)

            # Save outputs
            generator.save_curriculum_to_json(curriculum)
            generator.generate_markdown_curriculum(curriculum)

            print(f"\n✅ Curriculum generated successfully!")
            print(f"📁 Output directory: {generator.output_dir}/")

        except json.JSONDecodeError:
            print("❌ Invalid JSON file")
        except Exception as e:
            print(f"\n❌ Error: {str(e)}")

    def generate_by_topic(self):
        """Generate curriculum by specifying a topic."""
        print("\n📚 Generate Curriculum by Topic")
        print("-" * 50)

        topic = self.get_user_choice("Enter topic (e.g., 'Python Decorators'): ")

        print("\nSelect domain:")
        print("1. Python")
        print("2. TypeScript")
        print("3. AI/ML")
        domain_choice = self.get_user_choice("Choose domain (1-3): ")

        domains = {"1": "python", "2": "typescript", "3": "aiml"}
        domain = domains.get(domain_choice, "python")

        # Get difficulty
        print("\nSelect difficulty:")
        print("1. Beginner")
        print("2. Intermediate")
        print("3. Advanced")
        diff_choice = self.get_user_choice("Choose difficulty (1-3): ")

        difficulties = {"1": "beginner", "2": "intermediate", "3": "advanced"}
        difficulty = difficulties.get(diff_choice, "intermediate")

        print(f"\n⏳ Generating {difficulty} {domain} curriculum on '{topic}'...")

        # Create outline
        outline = {
            "course_name": f"{topic} - {difficulty.title()}",
            "course_code": f"COURSE-{topic[:6].upper()}",
            "level": difficulty.title(),
            "duration_weeks": 4,
            "units": [
                {
                    "name": f"Introduction to {topic}",
                    "description": f"Learn the fundamentals of {topic}",
                    "duration_weeks": 1,
                    "topics": [
                        {"name": f"{topic} Basics", "num_lessons": 2, "num_problems": 3},
                        {"name": f"{topic} Patterns", "num_lessons": 2, "num_problems": 3}
                    ]
                },
                {
                    "name": f"Advanced {topic}",
                    "description": f"Master advanced {topic} concepts",
                    "duration_weeks": 2,
                    "topics": [
                        {"name": f"{topic} Best Practices", "num_lessons": 3, "num_problems": 4},
                        {"name": f"{topic} Real-World Applications", "num_lessons": 2, "num_problems": 3}
                    ]
                }
            ]
        }

        try:
            generator = ContentGenerator(domain=domain)
            curriculum = generator.generate_curriculum_recursive(outline)

            generator.save_curriculum_to_json(curriculum)
            generator.generate_markdown_curriculum(curriculum)

            print(f"\n✅ Curriculum generated successfully!")
            print(f"📁 Output directory: {generator.output_dir}/")

        except Exception as e:
            print(f"\n❌ Error: {str(e)}")

    def list_repositories(self):
        """List available learning repositories."""
        print("\n📚 Available Learning Repositories")
        print("-" * 50)

        gen = CurriculumGenerator()

        print("\n🔷 TypeScript Repositories:")
        for i, repo in enumerate(gen.TYPESCRIPT_REPOS, 1):
            print(f"   {i}. {repo.name} (⭐ {repo.stars:,})")
            print(f"      Level: {repo.level} | {repo.best_for}")

        print("\n🔷 Python Repositories:")
        for i, repo in enumerate(gen.PYTHON_REPOS, 1):
            print(f"   {i}. {repo.name} (⭐ {repo.stars:,})")
            print(f"      Level: {repo.level} | {repo.best_for}")

        print("\n🔷 AI/ML Repositories:")
        for i, repo in enumerate(gen.AIML_REPOS, 1):
            print(f"   {i}. {repo.name} (⭐ {repo.stars:,})")
            print(f"      Level: {repo.level} | {repo.best_for}")

        print(f"\n📊 Total: {len(gen.all_repos)} repositories")

    def view_agent_skills(self):
        """View available agent skills."""
        print("\n🤖 Agent Skills Overview")
        print("-" * 50)

        skills_info = {
            "Curriculum Architect": [
                "analyze_github_repo - Extract concepts from repositories",
                "discover_learning_resources - Find learning repositories",
                "calculate_difficulty_progression - Scale difficulty automatically"
            ],
            "Lesson Generator": [
                "generate_lesson_content - Create detailed lessons",
                "generate_code_walkthrough - Create code walkthroughs",
                "generate_key_takeaways - Generate key takeaways"
            ],
            "Problem Creator": [
                "generate_progressive_problems - Create exercises with difficulty scaling",
                "create_quiz_from_content - Generate quiz questions",
                "generate_acceptance_criteria - Define success criteria"
            ],
            "Project Designer": [
                "design_project_from_repo - Create capstone projects",
                "generate_unit_project - Generate unit-level projects",
                "generate_getting_started_guide - Create getting started guides"
            ],
            "Assessment Grader": [
                "generate_answer_key - Create answer keys with explanations"
            ]
        }

        for agent, skills in skills_info.items():
            print(f"\n🔹 {agent}:")
            for skill in skills:
                print(f"   • {skill}")

        print(f"\n📊 Total: {sum(len(s) for s in skills_info.values())} skills available")

    def settings(self):
        """Configure settings."""
        print("\n⚙️  Settings")
        print("-" * 50)
        print(f"1. GitHub Token: {'✓ Set' if self.github_token else '✗ Not set'}")
        print(f"2. Output Directory: {self.output_dir}")
        print("0. Back to main menu")

        choice = self.get_user_choice("\nEnter choice: ")

        if choice == "1":
            token = self.get_user_choice("Enter GitHub token (or press Enter to skip): ")
            if token:
                self.github_token = token
                print("✓ Token set successfully")
            else:
                print("✓ Token unchanged")
        elif choice == "2":
            new_dir = self.get_user_choice(f"Enter output directory [{self.output_dir}]: ")
            if new_dir:
                self.output_dir = Path(new_dir)
                self.output_dir.mkdir(exist_ok=True)
                print(f"✓ Output directory set to: {self.output_dir}")

    def _print_curriculum_summary(self, curriculum: Dict[str, Any]):
        """Print curriculum summary."""
        print("\n📊 Curriculum Summary:")
        print(f"   Course: {curriculum.get('course_name', 'Unknown')}")
        print(f"   Duration: {curriculum.get('duration_weeks', 0)} weeks")

        if 'modules' in curriculum:
            total_lessons = sum(len(m.get('lessons', [])) for m in curriculum['modules'])
            total_problems = sum(len(m.get('problems', [])) for m in curriculum['modules'])
            print(f"   Modules: {len(curriculum['modules'])}")
            print(f"   Lessons: {total_lessons}")
            print(f"   Problems: {total_problems}")

    def run_tui(self):
        """Run the Terminal User Interface."""
        self.print_banner()

        while True:
            self.print_menu()
            choice = self.get_user_choice()

            if choice == "0":
                print("\n👋 Goodbye!")
                break
            elif choice == "1":
                self.generate_from_github()
            elif choice == "2":
                self.generate_from_outline()
            elif choice == "3":
                self.generate_by_topic()
            elif choice == "4":
                self.list_repositories()
            elif choice == "5":
                self.view_agent_skills()
            elif choice == "6":
                self.settings()
            else:
                print("❌ Invalid choice. Please try again.")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="AI-Powered Curriculum Generator",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python run.py                      # Run TUI
  python run.py --repo pytorch/pytorch  # Generate from GitHub repo
  python run.py --outline outline.json  # Generate from outline
  python run.py --topic "Python Decorators"  # Generate by topic
  python run.py --list               # List repositories
        """
    )

    parser.add_argument(
        "--repo",
        help="GitHub repository (owner/name)"
    )
    parser.add_argument(
        "--outline",
        help="Path to outline JSON file"
    )
    parser.add_argument(
        "--topic",
        help="Topic to generate curriculum for"
    )
    parser.add_argument(
        "--domain",
        choices=["python", "typescript", "aiml"],
        default="python",
        help="Domain for curriculum (default: python)"
    )
    parser.add_argument(
        "--level",
        choices=["beginner", "intermediate", "advanced"],
        default="intermediate",
        help="Difficulty level (default: intermediate)"
    )
    parser.add_argument(
        "--token",
        help="GitHub API token"
    )
    parser.add_argument(
        "--output",
        help="Output directory",
        default="output"
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="List available repositories"
    )

    args = parser.parse_args()

    runner = CurriculumRunner()
    runner.github_token = args.token
    runner.output_dir = Path(args.output)
    runner.output_dir.mkdir(exist_ok=True)

    # Handle command line arguments
    if args.list:
        runner.list_repositories()
    elif args.repo:
        owner, repo_name = args.repo.split("/", 1)
        print(f"⏳ Generating curriculum for {owner}/{repo_name}...")

        try:
            analyzer = GitHubRepoAnalyzer(token=args.token)
            repo_analysis = analyzer.analyze_repository(owner, repo_name)

            generator = CurriculumFromRepoGenerator(repo_analysis)
            curriculum = generator.generate_curriculum()

            output_file = runner.output_dir / f"{repo_name}_curriculum.json"
            with open(output_file, 'w') as f:
                json.dump(curriculum, f, indent=2)

            print(f"✅ Curriculum saved to: {output_file}")

        except Exception as e:
            print(f"❌ Error: {e}")
            sys.exit(1)

    elif args.outline:
        outline_path = Path(args.outline)
        if not outline_path.exists():
            print(f"❌ File not found: {args.outline}")
            sys.exit(1)

        try:
            with open(outline_path, 'r') as f:
                outline = json.load(f)

            generator = ContentGenerator(domain=args.domain)
            curriculum = generator.generate_curriculum_recursive(outline)

            generator.save_curriculum_to_json(curriculum)
            generator.generate_markdown_curriculum(curriculum)

            print(f"✅ Curriculum generated in: {generator.output_dir}/")

        except Exception as e:
            print(f"❌ Error: {e}")
            sys.exit(1)

    elif args.topic:
        outline = {
            "course_name": f"{args.topic} - {args.level.title()}",
            "course_code": f"COURSE-{args.topic[:6].upper()}",
            "level": args.level.title(),
            "duration_weeks": 4,
            "units": [
                {
                    "name": f"Introduction to {args.topic}",
                    "description": f"Learn the fundamentals of {args.topic}",
                    "duration_weeks": 1,
                    "topics": [
                        {"name": f"{args.topic} Basics", "num_lessons": 2, "num_problems": 3},
                        {"name": f"{args.topic} Patterns", "num_lessons": 2, "num_problems": 3}
                    ]
                },
                {
                    "name": f"Advanced {args.topic}",
                    "description": f"Master advanced {args.topic} concepts",
                    "duration_weeks": 2,
                    "topics": [
                        {"name": f"{args.topic} Best Practices", "num_lessons": 3, "num_problems": 4},
                        {"name": f"{args.topic} Real-World Applications", "num_lessons": 2, "num_problems": 3}
                    ]
                }
            ]
        }

        try:
            generator = ContentGenerator(domain=args.domain)
            curriculum = generator.generate_curriculum_recursive(outline)

            generator.save_curriculum_to_json(curriculum)
            generator.generate_markdown_curriculum(curriculum)

            print(f"✅ Curriculum generated in: {generator.output_dir}/")

        except Exception as e:
            print(f"❌ Error: {e}")
            sys.exit(1)

    else:
        # Run TUI
        runner.run_tui()


if __name__ == "__main__":
    main()