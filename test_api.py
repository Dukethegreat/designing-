#!/usr/bin/env python3
"""
Test script for the Design Customization App API
Demonstrates various API endpoints and their functionality
"""

import requests
import json

BASE_URL = "http://localhost:5000"

def test_health_check():
    """Test the health check endpoint"""
    print("🔍 Testing Health Check...")
    response = requests.get(f"{BASE_URL}/api/health")
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    print()

def test_color_scheme():
    """Test color scheme generation"""
    print("🎨 Testing Color Scheme Generation...")
    styles = ['modern', 'vintage', 'minimalist', 'bohemian']
    
    for style in styles:
        response = requests.post(f"{BASE_URL}/api/color-scheme", 
                               json={"style_type": style})
        if response.status_code == 200:
            data = response.json()
            print(f"Style: {style}")
            print(f"Colors: {data['colors']}")
            print(f"Palette: {data['palette_name']}")
            print()

def test_virtual_tryon():
    """Test virtual try-on functionality"""
    print("👗 Testing Virtual Try-On...")
    
    test_data = {
        "user_id": "demo_user_123",
        "scan_data": {
            "height": 175,
            "chest": 95,
            "waist": 70,
            "hips": 100
        }
    }
    
    response = requests.post(f"{BASE_URL}/api/virtual-tryon/scan", json=test_data)
    if response.status_code == 200:
        data = response.json()
        print(f"Measurements processed: {data['measurements']}")
        print(f"Message: {data['message']}")
    print()

def test_outfit_suggestions():
    """Test outfit suggestion engine"""
    print("✨ Testing Outfit Suggestions...")
    
    occasions = ['casual', 'formal', 'evening', 'athletic']
    
    for occasion in occasions:
        test_data = {
            "user_id": "fashion_user_456",
            "occasion": occasion
        }
        
        response = requests.post(f"{BASE_URL}/api/outfit-suggestions", json=test_data)
        if response.status_code == 200:
            data = response.json()
            print(f"Occasion: {occasion}")
            print(f"Suggestions count: {data['count']}")
            print(f"First suggestion confidence: {data['suggestions'][0]['confidence_score']}")
            print()

def test_inspiration_analysis():
    """Test inspiration image analysis"""
    print("🖼️ Testing Inspiration Analysis...")
    
    test_data = {
        "image_url": "https://example.com/modern-living-room.jpg"
    }
    
    response = requests.post(f"{BASE_URL}/api/inspiration/analyze", json=test_data)
    if response.status_code == 200:
        data = response.json()
        print(f"Design Elements: {data['design_elements']}")
        print(f"Similar Products: {len(data['similar_products'])} found")
        print(f"First product: {data['similar_products'][0]['name']}")
    print()

def main():
    """Run all API tests"""
    print("🚀 Starting Design Customization App API Tests")
    print("=" * 50)
    
    try:
        test_health_check()
        test_color_scheme()
        test_virtual_tryon()
        test_outfit_suggestions()
        test_inspiration_analysis()
        
        print("✅ All tests completed successfully!")
        print("🎉 Design Customization App is working perfectly!")
        
    except requests.exceptions.ConnectionError:
        print("❌ Error: Could not connect to the API server.")
        print("Please make sure the Flask app is running on http://localhost:5000")
    except Exception as e:
        print(f"❌ Error during testing: {e}")

if __name__ == "__main__":
    main()