#!/usr/bin/env python3
"""
Firebase Credentials Converter
Converts Firebase service account JSON file to environment variables format
"""

import json
import os
import sys

def convert_firebase_credentials(json_file_path):
    """Convert Firebase credentials JSON to environment variables format."""
    
    try:
        # Read the JSON file
        with open(json_file_path, 'r') as f:
            credentials = json.load(f)
        
        print("🔧 Converting Firebase credentials to environment variables...\n")
        
        # Define the required fields
        required_fields = [
            "type", "project_id", "private_key_id", "private_key",
            "client_email", "client_id", "auth_uri", "token_uri",
            "auth_provider_x509_cert_url", "client_x509_cert_url", "universe_domain"
        ]
        
        # Check if all required fields are present
        missing_fields = [field for field in required_fields if field not in credentials]
        if missing_fields:
            print(f"❌ Missing required fields: {', '.join(missing_fields)}")
            return False
        
        print("📋 Environment Variables for Render Dashboard:\n")
        print("Copy and paste these into your Render environment variables:\n")
        
        # Generate environment variables
        for field in required_fields:
            value = credentials[field]
            
            # Handle special cases
            if field == "private_key":
                # Replace newlines with \\n for environment variables
                value = value.replace('\n', '\\n')
            
            print(f"{field}={value}")
        
        print("\n" + "="*50)
        print("📝 Instructions:")
        print("1. Copy each line above")
        print("2. Go to your Render service dashboard")
        print("3. Navigate to Environment tab")
        print("4. Add each variable with its corresponding value")
        print("5. For 'private_key', make sure to keep the \\n format")
        print("6. Deploy your service")
        print("="*50)
        
        return True
        
    except FileNotFoundError:
        print(f"❌ File not found: {json_file_path}")
        return False
    except json.JSONDecodeError:
        print(f"❌ Invalid JSON file: {json_file_path}")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def main():
    """Main function."""
    print("🍎 Firebase Credentials Converter for Nutrio Bot")
    print("="*50)
    
    if len(sys.argv) != 2:
        print("Usage: python convert_firebase_credentials.py <path_to_firebase_credentials.json>")
        print("\nExample:")
        print("python convert_firebase_credentials.py firebase_credidentials.json")
        sys.exit(1)
    
    json_file_path = sys.argv[1]
    
    if convert_firebase_credentials(json_file_path):
        print("\n✅ Conversion completed successfully!")
    else:
        print("\n❌ Conversion failed!")
        sys.exit(1)

if __name__ == "__main__":
    main() 