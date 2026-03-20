#!/bin/bash
# 🔄 Curriculum Validation Script
# Run this to validate the curriculum system structure and content

echo "=========================================="
echo "  Curriculum System Validation"
echo "=========================================="
echo ""

# Colors for output
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Counters
PASSED=0
FAILED=0
WARNINGS=0

# Function to check if file exists
check_file() {
    if [ -f "$1" ]; then
        echo -e "${GREEN}✓${NC} $2"
        ((PASSED++))
    else
        echo -e "${RED}✗${NC} $2 (missing: $1)"
        ((FAILED++))
    fi
}

# Function to check if directory exists
check_dir() {
    if [ -d "$1" ]; then
        echo -e "${GREEN}✓${NC} $2"
        ((PASSED++))
    else
        echo -e "${RED}✗${NC} $2 (missing: $1)"
        ((FAILED++))
    fi
}

# Function to check file content
check_content() {
    if grep -q "$2" "$1" 2>/dev/null; then
        echo -e "${GREEN}✓${NC} $3"
        ((PASSED++))
    else
        echo -e "${YELLOW}⚠${NC} $3 (content not found in $1)"
        ((WARNINGS++))
    fi
}

echo "📁 Checking Directory Structure..."
echo "----------------------------------------"
check_dir "course-curriculum" "Main curriculum directory"
check_dir "course-curriculum/agents" "Agents directory"
check_dir "course-curriculum/curriculum" "Curriculum modules directory"
check_dir "course-curriculum/grading" "Grading directory"
check_dir "course-curriculum/progress" "Progress directory"
check_dir "course-curriculum/skills" "Skills directory"
check_dir "course-curriculum/tools" "Tools directory"
echo ""

echo "📄 Checking Core Files..."
echo "----------------------------------------"
check_file "course-curriculum/README.md" "README.md"
check_file "course-curriculum/SYSTEM.md" "SYSTEM.md"
check_file "course-curriculum/CONTEXT.md" "CONTEXT.md"
echo ""

echo "🤖 Checking Agent Files..."
echo "----------------------------------------"
check_file "course-curriculum/agents/orchestrator.md" "Orchestrator agent"
check_file "course-curriculum/agents/curriculum-architect.md" "Curriculum Architect agent"
check_file "course-curriculum/agents/lesson-generator.md" "Lesson Generator agent"
check_file "course-curriculum/agents/problem-creator.md" "Problem Creator agent"
check_file "course-curriculum/agents/project-designer.md" "Project Designer agent"
check_file "course-curriculum/agents/assessment-grader.md" "Assessment Grader agent"
check_file "course-curriculum/agents/mentor-agent.md" "Mentor Agent"
echo ""

echo "📚 Checking Curriculum Modules..."
echo "----------------------------------------"
check_file "course-curriculum/curriculum/ai-programming.md" "AI Programming module"
echo ""

echo "📊 Checking Support Files..."
echo "----------------------------------------"
check_file "course-curriculum/grading/rubrics.md" "Grading rubrics"
check_file "course-curriculum/progress/tracker.md" "Progress tracker"
check_file "course-curriculum/skills/definitions.md" "Skills definitions"
check_file "course-curriculum/tools/definitions.md" "Tools definitions"
echo ""

echo "🔍 Checking Agent Content..."
echo "----------------------------------------"
check_content "course-curriculum/agents/orchestrator.md" "name: orchestrator" "Orchestrator has name"
check_content "course-curriculum/agents/orchestrator.md" "## Purpose" "Orchestrator has purpose"
check_content "course-curriculum/agents/curriculum-architect.md" "name: curriculum-architect" "Architect has name"
check_content "course-curriculum/agents/lesson-generator.md" "name: lesson-generator" "Generator has name"
check_content "course-curriculum/agents/problem-creator.md" "name: problem-creator" "Creator has name"
check_content "course-curriculum/agents/project-designer.md" "name: project-designer" "Designer has name"
check_content "course-curriculum/agents/assessment-grader.md" "name: assessment-grader" "Grader has name"
check_content "course-curriculum/agents/mentor-agent.md" "name: mentor-agent" "Mentor has name"
echo ""

echo "📋 Checking Context File..."
echo "----------------------------------------"
check_content "course-curriculum/CONTEXT.md" "## 🎯 Project Identity" "Context has project identity"
check_content "course-curriculum/CONTEXT.md" "## 🏗️ System Architecture" "Context has architecture"
check_content "course-curriculum/CONTEXT.md" "## 📁 File Structure" "Context has file structure"
check_content "course-curriculum/CONTEXT.md" "## 🎓 Curriculum Modules" "Context has curriculum modules"
echo ""

echo "=========================================="
echo "  Validation Summary"
echo "=========================================="
echo -e "${GREEN}Passed:${NC}   $PASSED"
echo -e "${YELLOW}Warnings:${NC} $WARNINGS"
echo -e "${RED}Failed:${NC}   $FAILED"
echo ""

if [ $FAILED -eq 0 ]; then
    echo -e "${GREEN}✅ All critical checks passed!${NC}"
    exit 0
else
    echo -e "${RED}❌ Some checks failed. Please fix the issues above.${NC}"
    exit 1
fi