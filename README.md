# 🍎 Nutrio - Nutrition Assistant Telegram Bot

A comprehensive nutrition assistant for Indian users in Maharashtra and Karnataka, built with Python Telegram Bot v20+ and Firebase integration.

## 🚀 Features

### 🎯 Core Features
- **Personalized Meal Planning**: AI-powered meal suggestions based on user preferences
- **Regional Cuisine**: Karnataka and Maharashtra specific meal recommendations
- **Dietary Preferences**: Support for Vegetarian, Non-vegetarian, Jain, and Vegan diets
- **Health Considerations**: Meal filtering based on medical conditions (Diabetes, Thyroid, etc.)
- **Grocery Shopping**: Smart ingredient lists with cart functionality
- **External Integration**: Direct links to Blinkit and Zepto for ordering

### 🎮 Gamification
- **Streak System**: Daily engagement tracking with consecutive day bonuses
- **Points System**: Exponential point rewards for maintaining streaks
- **Profile Management**: Comprehensive user profiles with statistics

### 🛒 Shopping Features
- **Smart Cart**: Toggle-based item selection
- **Ingredient Lists**: Auto-generated from meal plans
- **Custom Lists**: Add/remove items manually
- **Order Integration**: Direct links to delivery services

## 📋 Prerequisites

- Python 3.8+
- Telegram Bot Token (from @BotFather)
- Firebase Project (optional, for data persistence)

## 🛠️ Installation

### 1. Clone the Repository
```bash
git clone <repository-url>
cd nutrio
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Environment Setup
```bash
# Copy the environment template
cp env_example.txt .env

# Edit .env file with your configuration
nano .env
```

### 4. Configure Environment Variables
```env
# Required
BOT_TOKEN=your_telegram_bot_token_here

# Optional (for Firebase)
FIREBASE_CREDENTIALS_PATH=firebase-credentials.json
```

### 5. Get Telegram Bot Token
1. Message @BotFather on Telegram
2. Send `/newbot` or use existing bot
3. Copy the token and add to `.env` file

### 6. Firebase Setup (Optional)
1. Create a Firebase project
2. Download service account key
3. Save as `firebase-credentials.json`
4. Update `FIREBASE_CREDENTIALS_PATH` in `.env`

## 🚀 Running the Bot

### Development Mode
```bash
python main.py
```

### Production Mode
```bash
# Use a process manager like PM2 or systemd
python main.py
```

## 📁 Project Structure

```
nutrio/
├── main.py                 # Main bot application
├── requirements.txt        # Python dependencies
├── .env                   # Environment variables (create from env_example.txt)
├── karnataka.json         # Karnataka meal data
├── maharastra.json        # Maharashtra meal data
├── firebase-credentials.json  # Firebase credentials (optional)
└── README.md              # This file
```

## 🎯 Usage

### Starting the Bot
1. Send `/start` to your bot
2. Follow the profile creation flow (7 steps)
3. Get personalized meal recommendations

### Available Commands
- `/start` - Start the bot and create profile
- `/cancel` - Cancel current operation

### Main Features
- **Daily Meal Plans**: Get personalized daily meal suggestions
- **Weekly Plans**: View 7-day meal plans
- **Grocery Lists**: Generate shopping lists from meal plans
- **Cart Management**: Add/remove items and order online
- **Profile Management**: View and update your preferences
- **Streak Tracking**: Monitor your daily engagement

## 🔧 Configuration

### Rate Limiting
- **Window**: 60 seconds
- **Max Requests**: 30 per window
- **Purpose**: Prevent abuse and ensure smooth operation

### Data Storage
- **Primary**: In-memory storage (fast access)
- **Backup**: Firebase Firestore (persistent)
- **Fallback**: Local JSON files for meal data

### Meal Data Format
```json
{
  "Food Item": "Dish Name",
  "Ingredients": ["ingredient1", "ingredient2"],
  "approx_calories": 250,
  "Health Impact": "Nutritional benefits",
  "Calorie Level": "low|medium|high"
}
```

## 🛡️ Security Features

### Input Validation
- **Name**: Alphanumeric + spaces, 2-50 characters
- **Age**: Numeric, 1-120 range
- **Medical**: Sanitized text, 3-200 characters

### Rate Limiting
- Per-user request tracking
- Automatic window reset
- Graceful rate limit handling

### Data Protection
- Environment variable configuration
- Input sanitization
- Error handling without data exposure

## 🔄 Error Handling

### Graceful Degradation
- **Missing JSON Files**: Fallback meal data
- **Firebase Unavailable**: Memory-only mode
- **Invalid Input**: Clear error messages with retry options

### Logging
- **Level**: INFO and above
- **Format**: Timestamp, logger, level, message
- **Purpose**: Debugging and monitoring

## 🚨 Troubleshooting

### Common Issues

#### Bot Token Error
```
❌ ERROR: BOT_TOKEN environment variable not set!
```
**Solution**: Add your bot token to the `.env` file

#### Missing Dependencies
```
Import "telegram" could not be resolved
```
**Solution**: Run `pip install -r requirements.txt`

#### Firebase Connection Failed
```
❌ Firebase connection failed
```
**Solution**: Check credentials file path and format

#### Rate Limit Exceeded
```
⚠️ Rate Limit Exceeded
```
**Solution**: Wait 60 seconds before making more requests

### Debug Mode
Enable debug logging by modifying the logging level in `main.py`:
```python
logging.basicConfig(level=logging.DEBUG)
```

## 📊 Performance

### Memory Usage
- **Per User**: ~2KB (profile + cart + streak data)
- **Total**: Scales with active users
- **Optimization**: Automatic cleanup of inactive sessions

### Response Time
- **Typical**: <500ms for most operations
- **Meal Generation**: <1s with JSON data
- **Firebase Operations**: <2s (when available)

## 🔮 Future Enhancements

### Planned Features
- [ ] Multi-language support
- [ ] More regional cuisines
- [ ] Nutritional analysis
- [ ] Recipe sharing
- [ ] Community features
- [ ] Advanced analytics

### Technical Improvements
- [ ] Database optimization
- [ ] Caching layer
- [ ] API rate limiting
- [ ] Webhook support
- [ ] Docker deployment

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

For support and questions:
- Create an issue on GitHub
- Check the troubleshooting section
- Review the error logs

## 🙏 Acknowledgments

- Python Telegram Bot community
- Firebase team
- Indian cuisine experts
- Beta testers and feedback providers

---

**Made with ❤️ for healthy eating in India** #   n u t r i o  
 #   n u t r i o  
 