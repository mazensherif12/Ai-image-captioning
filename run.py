"""
🎯 MAIN SCRIPT - Arabic Image Captioning
Run this file for everything!
"""

import os
import sys

# Add code directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'code'))

def main():
    print("\n" + "="*70)
    print("🎯 ARABIC IMAGE CAPTIONING")
    print("="*70)
    
    print("\nWhat do you want to do?")
    print("1. Train the model")
    print("2. Test the model")
    print("3. Show GUI")
    print("4. Exit")
    
    choice = input("\nEnter your choice (1-4): ")
    
    if choice == '1':
        print("\n🚀 TRAINING MODEL...")
        try:
            from train import train_model
            train_model()
        except Exception as e:
            print(f"❌ Error: {e}")
            import traceback
            traceback.print_exc()
    
    elif choice == '2':
        print("\n🧪 TESTING MODEL...")
        try:
            from test import test_model
            test_model()
        except Exception as e:
            print(f"❌ Error: {e}")
            import traceback
            traceback.print_exc()
    
    elif choice == '3':
        print("\n🖼️  SHOWING GUI...")
        try:
            from gui import show_gui
            show_gui()
        except Exception as e:
            print(f"❌ Error: {e}")
            import traceback
            traceback.print_exc()
    
    elif choice == '4':
        print("Goodbye!")
    
    else:
        print("❌ Invalid choice")
    
    print("\n" + "="*70)
    print("✅ DONE!")
    print("="*70)

if __name__ == "__main__":
    main()