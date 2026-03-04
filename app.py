from flask import Flask, render_template_string
import qrcode

app = Flask(__name__)

# HTML Design
html_page = """
<!DOCTYPE html>
<html>
<head>
<title>Vedika Love Surprise 💖</title>
<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  background: linear-gradient(135deg, #ff758c 0%, #ff7eb3 100%);
  text-align: center;
  font-family: 'Arial', sans-serif;
  color: white;
  min-height: 100vh;
  overflow: hidden;
  position: relative;
}

.heart {
  position: absolute;
  color: red;
  font-size: 30px;
  animation: float 6s infinite;
  opacity: 0.7;
}

@keyframes float {
  0% { transform: translateY(100vh) translateX(0) rotate(0deg); opacity: 1; }
  100% { transform: translateY(-100vh) translateX(100px) rotate(360deg); opacity: 0; }
}

.container {
  position: relative;
  z-index: 10;
  padding: 20px;
  margin-top: 40px;
}

h1 {
  font-size: 50px;
  margin-bottom: 20px;
  animation: glow 1.5s infinite alternate;
}

.big-heart {
  font-size: 100px;
  animation: beat 1s infinite;
  margin-bottom: 20px;
}

@keyframes beat {
  0%,100% { transform: scale(1); }
  50% { transform: scale(1.2); }
}

@keyframes glow {
  from { text-shadow: 0 0 10px white, 0 0 20px red; }
  to { text-shadow: 0 0 20px white, 0 0 40px red, 0 0 60px red; }
}

p {
  font-size: 22px;
  margin: 15px 0;
  animation: pulse 2s infinite;
}

@keyframes pulse {
  0%, 100% { transform: scale(1); }
  50% { transform: scale(1.05); }
}

button {
  padding: 15px 30px;
  font-size: 18px;
  border-radius: 50px;
  border: none;
  background: white;
  color: red;
  cursor: pointer;
  margin: 10px;
  font-weight: bold;
  transition: all 0.3s ease;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
}

button:hover {
  background: red;
  color: white;
  transform: scale(1.1);
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.3);
}

button:active {
  transform: scale(0.98);
}

.countdown {
  font-size: 24px;
  margin: 30px 0;
  padding: 20px;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 15px;
  backdrop-filter: blur(10px);
}

.quote {
  font-style: italic;
  font-size: 18px;
  margin: 20px 0;
  opacity: 0.9;
}

.star {
  position: absolute;
  color: yellow;
  font-size: 20px;
  animation: twinkle 1.5s infinite;
}

@keyframes twinkle {
  0%, 100% { opacity: 0.3; }
  50% { opacity: 1; }
}

.qr-container {
  margin-top: 40px;
  padding: 20px;
  background: rgba(255, 255, 255, 0.2);
  border-radius: 15px;
  display: inline-block;
}

img {
  margin-top: 15px;
  border-radius: 15px;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
}

.love-message {
  font-size: 16px;
  margin: 20px 0;
  padding: 15px;
  background: rgba(255, 255, 255, 0.1);
  border-left: 5px solid white;
  border-radius: 5px;
  max-width: 500px;
  margin-left: auto;
  margin-right: auto;
}

audio {
  margin-top: 20px;
  width: 300px;
}

</style>
</head>
<body>

<div class="container">
  <div class="big-heart">❤️</div>
  <h1>I love you, baby 😘💕</h1>
  <p>You Are My Happiness 💖</p>
  
  <div class="dream-text">
    <p class="quote">"Every moment with you is a moment in paradise" ✨</p>
  </div>

  <div class="countdown" id="countdown"></div>

  <div class="love-message">
    "In your eyes, I found my home. In your heart, I found my love. In your soul, I found myself." 💝
  </div>

  <button onclick="showLove()">❤️ Show Love</button>
  <button onclick="playMusic()">🎵 Romantic Music</button>
  <button onclick="createFireworks()">🎆 Surprise!</button>
  <button onclick="generateRandomQuote()">💬 Love Quote</button>
  <button onclick="showAnniversary()">💝 Something More For You</button>
  
  <br><br>
  
  <audio id="audio" style="display:none;">
    <source src="https://www2.cs.uic.edu/~i101/SoundFiles/StarWars60.wav" type="audio/wav">
  </audio>

  <div class="qr-container">
    <p>Scan to Share the Love 💌</p>
    <img src="/qr" style="width:200px; height:200px;">
  </div>
</div>

<script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>

<script>
// Create floating hearts
function createHeart() {
  const heart = document.createElement('div');
  heart.classList.add('heart');
  heart.innerHTML = '💖';
  heart.style.left = Math.random() * 100 + 'vw';
  document.body.appendChild(heart);
  setTimeout(() => heart.remove(), 6000);
}

setInterval(createHeart, 800);

// Countdown Timer
function updateCountdown() {
  let countDate = new Date("Mar 9, 2026 00:00:00").getTime();
  let timer = setInterval(function() {
    let now = new Date().getTime();
    let distance = countDate - now;
    let days = Math.floor(distance / (1000 * 60 * 60 * 24));
    let hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    let minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    let seconds = Math.floor((distance % (1000 * 60)) / 1000);
    
    document.getElementById('countdown').innerHTML = 
      days + 'd ' + hours + 'h ' + minutes + 'm ' + seconds + 's Left For Our Special Moment 💕';
  }, 1000);
}
updateCountdown();

// Show Love
function showLove() {
  const messages = [
    "You make my heart skip a beat! 💗",
    "I love everything about you! 😍",
    "You're my greatest blessing! 🙏💕",
    "Forever isn't long enough with you! ♾️",
    "You complete me! 👫"
  ];
  const randomMsg = messages[Math.floor(Math.random() * messages.length)];
  alert(randomMsg);
  confetti();
}

// Play Music
function playMusic() {
  const audio = document.getElementById('audio');
  if (audio.paused) {
    audio.play();
    alert('🎵 Music Started! Enjoy the Vibes!');
  } else {
    audio.pause();
    alert('⏸️ Music Paused!');
  }
}

// Confetti Fireworks
function createFireworks() {
  confetti({
    particleCount: 150,
    spread: 100,
    origin: { y: 0.6 }
  });
  alert('🎆 Boom! You just made my heart explode with happiness! 💥💖');
}

// Love Quotes
const loveQuotes = [
  "Love is not about finding the right person, it's about being the right person for someone.",
  "You are my today and all of my tomorrows.",
  "I fall in love with you every single day.",
  "You're the best thing that ever happened to me.",
  "In your arms is exactly where I want to be.",
  "Love is when the other person's happiness is more important than your own.",
  "You make me want to be a better person."
];

function generateRandomQuote() {
  const quote = loveQuotes[Math.floor(Math.random() * loveQuotes.length)];
  alert('💕 ' + quote + ' 💕');
}

// Anniversary message
function showAnniversary() {
  alert("Happy Anniversary, my love 💕 😘 Every day with you feels like a beautiful dream.💗😘 Thank you for loving me, supporting me, and making my life so special. 💗I’m so lucky to have you forever by my side.🧿🥺You are not just my partner, you are my peace, my happiness, and my biggest blessing. 😘💗I promise to love you more with each passing day.😘💗Through every smile, every tear, every moment — I choose you. 💗🧿🥺Today, tomorrow, and always. I love you so much 😘💗");
}
</script>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(html_page)

@app.route("/qr")
def generate_qr():
    url = "http://127.0.0.1:5000/"
    qr = qrcode.make(url)
    qr.save("static_qr.png")
    return '<img src="/static_qr.png">'

if __name__ == "__main__":
    app.run(debug=True)
