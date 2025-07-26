# 🚀 Nutrio Bot Deployment Guide

## 📋 Prerequisites
- GitHub repository with your code
- Telegram Bot Token from [@BotFather](https://t.me/botfather)
- Firebase credentials file (`firebase_credidentials.json`)
- Render account (free tier available)

## 🎯 Deployment Options

### Option 1: Render Dashboard (Recommended for beginners)

#### Step 1: Prepare Your Repository
1. Ensure all files are in the repository root:
   ```
   📁 your-repo/
   ├── main.py
   ├── requirements.txt
   ├── runtime.txt
   ├── karnataka.json
   ├── maharastra.json
   ├── .gitignore
   └── README.md
   ```

#### Step 2: Create Render Service
1. Go to [Render Dashboard](https://dashboard.render.com)
2. Click "New" → "Background Worker"
3. Connect your GitHub repository
4. Configure the service:
   - **Name**: `nutrio-bot`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python main.py`
   - **Root Directory**: Leave blank (or delete if set)

#### Step 3: Set Environment Variables
In the Render dashboard, go to "Environment" tab:

**Required:**
- **BOT_TOKEN**: Your Telegram bot token

**Optional (for Firebase):**
- **type**: `service_account`
- **project_id**: Your Firebase project ID
- **private_key_id**: Your Firebase private key ID
- **private_key**: Your Firebase private key (with `\\n` for newlines)
- **client_email**: Your Firebase client email
- **client_id**: Your Firebase client ID
- **auth_uri**: `https://accounts.google.com/o/oauth2/auth`
- **token_uri**: `https://oauth2.googleapis.com/token`
- **auth_provider_x509_cert_url**: `https://www.googleapis.com/oauth2/v1/certs`
- **client_x509_cert_url**: Your Firebase client certificate URL
- **universe_domain**: `googleapis.com`

#### Step 4: Firebase Setup (Optional)
If you want Firebase functionality:
1. Go to Firebase Console → Project Settings → Service Accounts
2. Generate a new private key
3. Copy the values from the JSON file to the environment variables above
4. For `private_key`, replace actual newlines with `\\n`

#### Step 5: Deploy
1. Click "Create Background Worker"
2. Wait for build to complete
3. Check logs for successful startup

### Option 2: Infrastructure as Code (render.yaml)

#### Step 1: Use render.yaml
The `render.yaml` file is already configured. Simply:
1. Push your code to GitHub
2. In Render dashboard, create service from "Blueprint"
3. Select your repository
4. Render will automatically configure everything

### Option 3: Docker Deployment

#### Local Testing with Docker
```bash
# Build and run locally
docker-compose up --build

# Or build manually
docker build -t nutrio-bot .
docker run -e BOT_TOKEN=your_token nutrio-bot
```

#### Deploy Docker to Render
1. Create a "Web Service" instead of Background Worker
2. Set build command to: `docker build -t nutrio-bot .`
3. Set start command to: `docker run nutrio-bot`

## 🔧 Environment Variables

| Variable | Description | Required | Example |
|----------|-------------|----------|---------|
| `BOT_TOKEN` | Telegram bot token | ✅ | `1234567890:ABCdefGHIjklMNOpqrsTUVwxyz` |
| `type` | Firebase service account type | ❌ | `service_account` |
| `project_id` | Firebase project ID | ❌ | `your-project-123456` |
| `private_key_id` | Firebase private key ID | ❌ | `abc123def456...` |
| `private_key` | Firebase private key (with `\\n`) | ❌ | `-----BEGIN PRIVATE KEY-----\\n...\\n-----END PRIVATE KEY-----\\n` |
| `client_email` | Firebase client email | ❌ | `firebase-adminsdk@project.iam.gserviceaccount.com` |
| `client_id` | Firebase client ID | ❌ | `123456789012345678901` |
| `auth_uri` | Firebase auth URI | ❌ | `https://accounts.google.com/o/oauth2/auth` |
| `token_uri` | Firebase token URI | ❌ | `https://oauth2.googleapis.com/token` |
| `auth_provider_x509_cert_url` | Firebase auth provider cert URL | ❌ | `https://www.googleapis.com/oauth2/v1/certs` |
| `client_x509_cert_url` | Firebase client cert URL | ❌ | `https://www.googleapis.com/robot/v1/metadata/x509/...` |
| `universe_domain` | Firebase universe domain | ❌ | `googleapis.com` |

## 📁 File Structure for Deployment

```
📁 Repository Root/
├── main.py                    # Main bot code
├── requirements.txt           # Python dependencies
├── runtime.txt               # Python version (3.10.14)
├── render.yaml              # Render configuration
├── Dockerfile               # Docker configuration
├── docker-compose.yml       # Local Docker setup
├── .dockerignore           # Docker ignore rules
├── .gitignore             # Git ignore rules
├── karnataka.json         # Karnataka meal data
├── maharastra.json        # Maharashtra meal data
├── README.md              # Project documentation
├── LICENSE                # License file
├── CODE_OF_CONDUCT.md     # Community guidelines
├── CONTRIBUTING.md        # Contribution guidelines
└── DEPLOYMENT.md          # This file
```

## 🚨 Common Issues & Solutions

### Issue: "Python version not supported"
**Solution**: Ensure `runtime.txt` contains `python-3.10.14` and is in the root directory.

### Issue: "Module not found"
**Solution**: Check `requirements.txt` includes all dependencies:
```
python-telegram-bot==20.7
python-dotenv==1.0.0
firebase-admin==6.2.0
```

### Issue: "Bot token not found"
**Solution**: Set `BOT_TOKEN` environment variable in Render dashboard.

### Issue: "Firebase credentials not found"
**Solution**: Upload `firebase_credidentials.json` as a Secret File in Render.

### Issue: "Root directory not found"
**Solution**: Clear the "Root Directory" setting in Render (leave it blank).

## 🔍 Monitoring & Logs

### View Logs in Render
1. Go to your service in Render dashboard
2. Click "Logs" tab
3. Look for startup messages:
   ```
   ✅ Firebase connected successfully
   🤖 Nutrio Bot is starting...
   ```

### Health Checks
The bot includes built-in health checks:
- Python version validation
- Bot token validation
- Firebase connection check
- Rate limiting protection

## 🔄 Updates & Maintenance

### Update Bot Code
1. Push changes to GitHub
2. Render automatically redeploys
3. Check logs for successful deployment

### Update Dependencies
1. Update `requirements.txt`
2. Push to GitHub
3. Render rebuilds with new dependencies

### Environment Variable Changes
1. Update in Render dashboard
2. Service automatically restarts
3. No code push needed

## 🆘 Troubleshooting

### Bot Not Responding
1. Check Render logs for errors
2. Verify bot token is correct
3. Ensure bot is not blocked by users
4. Check if service is running (green status)

### Firebase Issues
1. Verify all Firebase environment variables are set correctly
2. Check Firebase project settings and service account permissions
3. Ensure Firestore is enabled in your Firebase project
4. Verify the `private_key` has `\\n` instead of actual newlines
5. Check network connectivity to Firebase services

### Performance Issues
1. Monitor Render service metrics
2. Check for memory leaks
3. Optimize meal data loading
4. Consider upgrading to paid plan

## 📞 Support

If you encounter issues:
1. Check Render documentation
2. Review bot logs for error messages
3. Verify all configuration steps
4. Test locally with Docker first

---

**🎉 Your Nutrio bot is now ready for production deployment!** 