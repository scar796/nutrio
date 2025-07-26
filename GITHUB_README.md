# 🍎 Nutrio - AI Nutrition Assistant Bot

> **🚀 Production Ready & Deployed on Render**  
> A smart Telegram bot that creates personalized meal plans for Indian users in Maharashtra and Karnataka.

[![Python](https://img.shields.io/badge/Python-3.10-blue.svg)](https://www.python.org/)
[![Telegram](https://img.shields.io/badge/Telegram-Bot-blue.svg)](https://core.telegram.org/bots/)
[![Firebase](https://img.shields.io/badge/Firebase-Database-orange.svg)](https://firebase.google.com/)
[![Render](https://img.shields.io/badge/Render-Deployed-green.svg)](https://render.com/)

## ✨ Features

- 🤖 **AI-Powered Meal Planning** - Personalized recommendations based on your profile
- 🏛️ **Regional Cuisine** - Specialized for Maharashtra and Karnataka
- 🥬 **Diet Support** - Vegetarian, Non-veg, Jain, and Vegan options
- 🏥 **Health-Aware** - Considers medical conditions like diabetes and thyroid
- 🔥 **Streak System** - Gamified nutrition tracking with points
- 🛒 **Smart Grocery Lists** - Auto-generated shopping lists with delivery links
- 📊 **Firebase Integration** - Persistent user profiles and data storage
- 🚀 **Production Ready** - Deployed on Render with Docker support

## 🚀 Quick Start

### For Users
1. Find the bot on Telegram
2. Send `/start` to begin
3. Complete your profile setup
4. Get personalized meal plans!

### For Developers

#### Prerequisites
- Python 3.10+
- Telegram Bot Token
- Firebase credentials (optional)

#### Local Setup
```bash
# Clone the repository
git clone https://github.com/yourusername/nutrio.git
cd nutrio

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp env_example.txt .env
# Edit .env with your BOT_TOKEN

# Run the bot
python main.py
```

#### Docker Setup
```bash
# Build and run with Docker
docker-compose up --build

# Or run directly
docker build -t nutrio-bot .
docker run -e BOT_TOKEN=your_token nutrio-bot
```

## 🚀 Deployment

### Render (Recommended)
1. Fork this repository
2. Create a new Background Worker on Render
3. Set environment variables:
   - **Required**: `BOT_TOKEN` (your Telegram bot token)
   - **Optional**: Firebase environment variables (see DEPLOYMENT.md for full list)
4. Deploy! 🎉

**Detailed deployment guide**: [DEPLOYMENT.md](DEPLOYMENT.md)

## 📁 Project Structure

```
📁 nutrio/
├── main.py                    # Main bot application
├── requirements.txt           # Python dependencies
├── runtime.txt               # Python version specification
├── render.yaml              # Render deployment config
├── Dockerfile               # Docker configuration
├── docker-compose.yml       # Local Docker setup
├── karnataka.json           # Karnataka meal database
├── maharastra.json          # Maharashtra meal database
├── .gitignore              # Git ignore rules
├── README.md               # This file
├── DEPLOYMENT.md           # Deployment guide
├── LICENSE                 # MIT License
├── CODE_OF_CONDUCT.md      # Community guidelines
└── CONTRIBUTING.md         # Contribution guidelines
```

## 🔧 Configuration

### Environment Variables
| Variable | Description | Required |
|----------|-------------|----------|
| `BOT_TOKEN` | Telegram bot token | ✅ |
| `type` | Firebase service account type | ❌ |
| `project_id` | Firebase project ID | ❌ |
| `private_key_id` | Firebase private key ID | ❌ |
| `private_key` | Firebase private key (with `\\n`) | ❌ |
| `client_email` | Firebase client email | ❌ |
| `client_id` | Firebase client ID | ❌ |
| `auth_uri` | Firebase auth URI | ❌ |
| `token_uri` | Firebase token URI | ❌ |
| `auth_provider_x509_cert_url` | Firebase auth provider cert URL | ❌ |
| `client_x509_cert_url` | Firebase client cert URL | ❌ |
| `universe_domain` | Firebase universe domain | ❌ |

### Features
- **Rate Limiting**: 30 requests per minute per user
- **Health Checks**: Built-in monitoring and validation
- **Error Handling**: Graceful fallbacks for missing data
- **Security**: Input validation and sanitization

## 🍽️ Meal Data

The bot uses regional meal databases:
- **Karnataka**: Traditional Karnataka cuisine with nutritional info
- **Maharashtra**: Authentic Maharashtra dishes with health benefits

Each meal includes:
- Ingredients list
- Calorie information
- Health impact details
- Dietary compatibility

## 🔥 Streak System

Users earn points for daily engagement:
- **Day 1**: 2-5 points
- **Day 2**: 4-8 points  
- **Day 3**: 8-15 points
- **Day 4+**: Exponential growth (1.5x multiplier)

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Development Setup
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test with Docker: `docker-compose up --build`
5. Submit a pull request

## 📊 Tech Stack

- **Backend**: Python 3.10
- **Bot Framework**: python-telegram-bot v20+
- **Database**: Firebase Firestore
- **Deployment**: Render (Background Worker)
- **Containerization**: Docker
- **Configuration**: Environment variables + dotenv

## 🛡️ Security

- ✅ Bot token protection via environment variables
- ✅ Firebase credentials secured as Secret Files
- ✅ Input validation and sanitization
- ✅ Rate limiting to prevent abuse
- ✅ No sensitive data in codebase

## 📈 Performance

- **Memory Efficient**: In-memory caching with Firebase persistence
- **Fast Response**: Optimized meal selection algorithms
- **Scalable**: Containerized deployment ready
- **Reliable**: Health checks and error handling

## 🆘 Support

- **Documentation**: [DEPLOYMENT.md](DEPLOYMENT.md)
- **Issues**: [GitHub Issues](https://github.com/yourusername/nutrio/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/nutrio/discussions)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Telegram Bot API for the platform
- Firebase for data persistence
- Render for hosting infrastructure
- Indian cuisine communities for meal data

---

**⭐ Star this repository if you find it helpful!**

**🤖 Ready to deploy? Check out [DEPLOYMENT.md](DEPLOYMENT.md) for step-by-step instructions!** 