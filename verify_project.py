#!/usr/bin/env python3
"""
GameSantai Final Verification Script
Checks if all components are properly set up
"""

import os
from pathlib import Path

class GameSantaiVerification:
    def __init__(self):
        self.project_root = Path("/app")
        self.passed = []
        self.failed = []
        self.warnings = []
    
    def check_file_exists(self, path, description):
        """Check if a file exists"""
        full_path = self.project_root / path
        if full_path.exists():
            self.passed.append(f"✅ {description}")
            return True
        else:
            self.failed.append(f"❌ {description} - File not found: {path}")
            return False
    
    def check_folder_exists(self, path, description):
        """Check if a folder exists"""
        full_path = self.project_root / path
        if full_path.exists() and full_path.is_dir():
            self.passed.append(f"✅ {description}")
            return True
        else:
            self.failed.append(f"❌ {description} - Folder not found: {path}")
            return False
    
    def verify_structure(self):
        """Verify folder structure"""
        print("📁 Verifying Folder Structure...")
        print("-" * 60)
        
        folders = [
            ("Assets/Scenes", "Scenes folder"),
            ("Assets/Scripts", "Scripts folder"),
            ("Assets/Scripts/Editor", "Editor scripts folder"),
            ("Assets/Characters", "Characters folder"),
            ("Assets/Characters/Models", "Character models folder"),
            ("Assets/Characters/Animations", "Animations folder"),
            ("Assets/Characters/Prefabs", "Character prefabs folder"),
            ("Assets/Environment/City", "Environment folder"),
            ("Assets/Environment/City/Materials", "Materials folder"),
            ("Assets/Environment/City/Prefabs", "Environment prefabs folder"),
        ]
        
        for folder, desc in folders:
            self.check_folder_exists(folder, desc)
        
        print()
    
    def verify_scene(self):
        """Verify scene file"""
        print("🎬 Verifying Scene...")
        print("-" * 60)
        
        self.check_file_exists("Assets/Scenes/01_Medieval_City.unity", "Main scene (01_Medieval_City.unity)")
        self.check_file_exists("Assets/Scenes/01_Medieval_City.unity.meta", "Scene meta file")
        
        print()
    
    def verify_scripts(self):
        """Verify C# scripts"""
        print("📝 Verifying Scripts...")
        print("-" * 60)
        
        scripts = [
            ("Assets/Scripts/PlayerController.cs", "PlayerController script"),
            ("Assets/Scripts/PlayerAnimatorController.cs", "PlayerAnimatorController script"),
            ("Assets/Scripts/ThirdPersonCamera.cs", "ThirdPersonCamera script"),
            ("Assets/Scripts/PlayerInputActions.inputactions", "Input Actions asset"),
            ("Assets/Scripts/Editor/GameSantaiEditorSetup.cs", "Editor setup tool"),
        ]
        
        for script, desc in scripts:
            if self.check_file_exists(script, desc):
                # Check if meta file exists
                self.check_file_exists(f"{script}.meta", f"{desc} meta file")
        
        print()
    
    def verify_guides(self):
        """Verify setup guides"""
        print("📖 Verifying Setup Guides...")
        print("-" * 60)
        
        guides = [
            ("Assets/Characters/CHARACTER_SETUP_GUIDE.md", "Character setup guide"),
            ("Assets/Environment/City/ENVIRONMENT_SETUP.md", "Environment setup guide"),
            ("SETUP_COMPLETE_README.md", "Main README"),
            ("verify_setup.py", "Setup script"),
        ]
        
        for guide, desc in guides:
            self.check_file_exists(guide, desc)
        
        print()
    
    def verify_unity_config(self):
        """Verify Unity configuration"""
        print("⚙️ Verifying Unity Configuration...")
        print("-" * 60)
        
        configs = [
            ("ProjectSettings/ProjectVersion.txt", "Project version"),
            ("ProjectSettings/EditorBuildSettings.asset", "Build settings"),
            ("Packages/manifest.json", "Package manifest"),
        ]
        
        for config, desc in configs:
            self.check_file_exists(config, desc)
        
        # Check Unity version
        version_file = self.project_root / "ProjectSettings/ProjectVersion.txt"
        if version_file.exists():
            with open(version_file, 'r') as f:
                content = f.read()
                if "6000.2.8f1" in content:
                    self.passed.append("✅ Unity version: 6000.2.8f1")
                else:
                    self.warnings.append(f"⚠️ Unity version might be different: {content}")
        
        print()
    
    def verify_git(self):
        """Verify git configuration"""
        print("🔧 Verifying Git Configuration...")
        print("-" * 60)
        
        if self.check_folder_exists(".git", "Git repository"):
            # Check current branch
            try:
                with open(self.project_root / ".git/HEAD", 'r') as f:
                    head = f.read().strip()
                    if "gamesantai" in head:
                        self.passed.append("✅ On branch: gamesantai")
                    else:
                        self.warnings.append(f"⚠️ Branch might be different: {head}")
            except:
                self.warnings.append("⚠️ Could not read branch information")
        
        print()
    
    def count_files(self):
        """Count created files"""
        print("📊 File Statistics...")
        print("-" * 60)
        
        cs_files = list((self.project_root / "Assets/Scripts").rglob("*.cs"))
        inputactions_files = list((self.project_root / "Assets/Scripts").rglob("*.inputactions"))
        scene_files = list((self.project_root / "Assets/Scenes").glob("01_Medieval_City.unity"))
        
        print(f"  📄 C# Scripts created: {len(cs_files)}")
        print(f"  🎮 Input Actions: {len(inputactions_files)}")
        print(f"  🎬 Scenes created: {len(scene_files)}")
        print()
    
    def print_summary(self):
        """Print verification summary"""
        print("\n" + "=" * 70)
        print("📋 VERIFICATION SUMMARY")
        print("=" * 70)
        
        print(f"\n✅ PASSED: {len(self.passed)} checks")
        for item in self.passed:
            print(f"  {item}")
        
        if self.warnings:
            print(f"\n⚠️ WARNINGS: {len(self.warnings)}")
            for item in self.warnings:
                print(f"  {item}")
        
        if self.failed:
            print(f"\n❌ FAILED: {len(self.failed)} checks")
            for item in self.failed:
                print(f"  {item}")
        
        print("\n" + "=" * 70)
        
        if not self.failed:
            print("🎉 ALL CHECKS PASSED!")
            print("✅ Project is ready to open in Unity Editor")
            print("\n📖 Next Steps:")
            print("  1. Open project in Unity Hub (Unity 6000.2.8f1)")
            print("  2. Wait for compilation to complete")
            print("  3. Run: Tools > GameSantai > Create Player Setup")
            print("  4. Press Play to test the prototype")
            print("\n📚 Read SETUP_COMPLETE_README.md for detailed instructions")
        else:
            print("⚠️ Some checks failed. Please review the errors above.")
        
        print("=" * 70 + "\n")
    
    def run(self):
        """Run all verifications"""
        print("\n" + "=" * 70)
        print("🔍 GAMESANTAI PROJECT VERIFICATION")
        print("=" * 70 + "\n")
        
        self.verify_structure()
        self.verify_scene()
        self.verify_scripts()
        self.verify_guides()
        self.verify_unity_config()
        self.verify_git()
        self.count_files()
        self.print_summary()
        
        return len(self.failed) == 0

if __name__ == "__main__":
    verifier = GameSantaiVerification()
    success = verifier.run()
    
    import sys
    sys.exit(0 if success else 1)
