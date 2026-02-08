"""
Deployment script for the AI Clothes Changer application
"""
import subprocess
import sys
import os

def install_requirements():
    """Install required packages"""
    print("Installing required packages...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    print("Requirements installed successfully!")

def run_application():
    """Run the main application"""
    print("Starting the AI Clothes Changer application...")
    print("Please wait while the application initializes...")
    print("This may take a few minutes on first run as models are downloaded...")
    
    # Import and run the main application directly
    try:
        import main
        main.main()
    except KeyboardInterrupt:
        print("\nApplication stopped by user.")
    except Exception as e:
        print(f"An error occurred: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    print("AI Clothes Changer - Deployment Script")
    print("="*50)
    
    # Ask user if they want to install requirements
    response = input("Would you like to install requirements first? (y/n): ")
    if response.lower() == 'y':
        install_requirements()
    
    print("\nLaunching the application...")
    run_application()