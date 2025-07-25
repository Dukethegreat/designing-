# 🎨 Design Customization App

A comprehensive Flask-based API platform for interior design, fashion, and jewelry customization with virtual try-on capabilities. The app features AI-powered design suggestions, color scheme generation, and intelligent outfit recommendations.

## ✨ Features

- **🎨 AI-Powered Color Schemes**: Generate beautiful color palettes based on different design styles
- **👗 Virtual Try-On**: Process body measurements and provide fit analysis
- **✨ Intelligent Outfit Suggestions**: Get personalized outfit recommendations for different occasions
- **🖼️ Inspiration Analysis**: Extract design elements from images and find similar products
- **📱 RESTful API**: Mobile-ready endpoints for easy integration
- **🔍 Health Monitoring**: Built-in system health checks

## 🚀 Quick Start

### Prerequisites

- Python 3.13+
- Virtual environment support

### Installation

1. **Clone or download the project files**
2. **Set up virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   python simple_app.py
   ```

5. **Access the application:**
   - Web Interface: http://localhost:5000
   - API Base URL: http://localhost:5000/api

## 📚 API Endpoints

### Health Check
```http
GET /api/health
```
Returns system status and timestamp.

### Color Scheme Generation
```http
POST /api/color-scheme
Content-Type: application/json

{
  "style_type": "modern"  // Options: modern, vintage, minimalist, bohemian
}
```

### Virtual Try-On Body Scan
```http
POST /api/virtual-tryon/scan
Content-Type: application/json

{
  "user_id": "user123",
  "scan_data": {
    "height": 175,
    "chest": 95,
    "waist": 70,
    "hips": 100
  }
}
```

### Outfit Suggestions
```http
POST /api/outfit-suggestions
Content-Type: application/json

{
  "user_id": "user123",
  "occasion": "formal"  // Options: casual, formal, evening, athletic
}
```

### Inspiration Image Analysis
```http
POST /api/inspiration/analyze
Content-Type: application/json

{
  "image_url": "https://example.com/image.jpg"
}
```

## 🧪 Testing

Run the comprehensive test suite:

```bash
python test_api.py
```

This will test all API endpoints and display the results.

### Manual Testing with curl

```bash
# Health check
curl -X GET http://localhost:5000/api/health

# Color scheme
curl -X POST -H "Content-Type: application/json" \
  -d '{"style_type": "vintage"}' \
  http://localhost:5000/api/color-scheme

# Outfit suggestions
curl -X POST -H "Content-Type: application/json" \
  -d '{"user_id": "test123", "occasion": "formal"}' \
  http://localhost:5000/api/outfit-suggestions
```

## 🏗️ Architecture

### Core Components

1. **DesignEngine**: Handles color palette generation and outfit suggestions
2. **VirtualTryOn**: Processes body measurements and fit analysis
3. **InspirationEngine**: Analyzes images and finds similar products

### Data Models

The application uses in-memory data structures for the simplified version. For production, these would be backed by a database:

- **StyleProfile**: User's design preferences and style DNA
- **User**: User account information and preferences
- **Design**: Custom design creations
- **WardrobeItem**: Individual clothing/accessory items

## 🔧 Configuration

### Environment Variables

- `FLASK_ENV`: Set to `development` for debug mode
- `FLASK_HOST`: Server host (default: 0.0.0.0)
- `FLASK_PORT`: Server port (default: 5000)

### Customization

The application can be extended with:

- **Database Integration**: Add SQLAlchemy models for persistent storage
- **Machine Learning**: Integrate ML models for better recommendations
- **Image Processing**: Add computer vision for real image analysis
- **Authentication**: Implement user authentication and authorization

## 📁 Project Structure

```
design-app/
├── simple_app.py          # Main Flask application
├── app.py                 # Full version with SQLAlchemy (for reference)
├── test_api.py           # Comprehensive API tests
├── requirements.txt      # Python dependencies
├── README.md            # This file
└── venv/               # Virtual environment (created during setup)
```

## 🎯 Use Cases

### Interior Design
- Generate color schemes for rooms
- Analyze inspiration images
- Find matching furniture and decor

### Fashion
- Virtual try-on for clothing
- Outfit suggestions for occasions
- Style DNA analysis

### Jewelry Design
- Color coordination with outfits
- Style matching for accessories
- Custom design recommendations

## 🔮 Future Enhancements

- **AI/ML Integration**: Real machine learning models for better predictions
- **Image Recognition**: Computer vision for actual image analysis
- **3D Visualization**: 3D room and outfit visualization
- **Social Features**: Share designs and get community feedback
- **Mobile App**: Native mobile applications
- **E-commerce Integration**: Direct product purchasing
- **AR/VR Support**: Augmented and virtual reality features

## 🛠️ Development

### Adding New Features

1. Create new endpoint functions in `simple_app.py`
2. Add corresponding tests in `test_api.py`
3. Update this README with new API documentation

### Database Integration

To add database support:

1. Uncomment SQLAlchemy imports in `app.py`
2. Configure database URI
3. Run database migrations
4. Update endpoints to use database models

## 📄 License

This project is provided as-is for educational and demonstration purposes.

## 🤝 Contributing

This is a demonstration project. For production use, consider:

- Adding proper error handling
- Implementing authentication
- Adding input validation
- Setting up logging
- Adding rate limiting
- Implementing caching

---

**🎉 Happy Designing!** The Design Customization App is ready to help you create amazing designs and outfit combinations!