import pandas as pd
import numpy as np
import os
from datetime import datetime, timedelta, timezone

# Define the directory to save the datasets
dataset_dir = os.path.dirname(__file__)

### 🔹 13 Grouped Emotion Categories (For UI Selection) ###
emotion_categories = [
    "Anxiety/Stress", "Sadness/Despair", "Anger/Resentment", "Happiness/Joy",
    "Disappointment/Regret", "Shame/Guilt", "Pride/Confidence", "Comparison/Social Pressure",
    "Empathy/Compassion", "Curiosity/Awe", "Belonging/Connection", "Nostalgia/Irony", "Love/Trust Issues"
]

# Expert-Recommended Activities & Descriptions for Each Emotion Category
activity_map = {
    "Anxiety/Stress": [
        "4-7-8 Breathing – Inhale for 4 sec, hold for 7 sec, exhale for 8 sec. Repeat 5 times.",
        "5-4-3-2-1 Grounding – Name 5 things you see, 4 you touch, 3 you hear, 2 you smell, 1 you taste.",
        "Progressive Muscle Relaxation – Tense each muscle for 5 sec, then release.",
        "Cold Water Splash – Splash cold water on your face to reset your nervous system.",
        "Write & Rip Technique – Write down worries and tear the paper. Imagine throwing stress away.",
        "Box Breathing – Inhale for 4 sec, hold for 4 sec, exhale for 4 sec, hold for 4 sec. Repeat 5 times.",
        "Listen to Nature Sounds – Play ocean waves or birds chirping for 5 minutes.",
        "Self-Hug – Wrap your arms around yourself and squeeze gently for 30 seconds.",
        "Rocking Motion – Sit and rock gently, or sway while standing to self-soothe.",
        "Stretching Routine – Stretch arms, neck, and legs to release physical tension."
    ],
    "Sadness/Despair": [
        "Warm Drink Ritual – Hold and sip a warm tea or coffee, focusing on the warmth and taste.",
        "List 3 Things You're Grateful For – Write 3 small positive things from today.",
        "Humming or Singing – Hum a tune or sing a song that makes you feel comforted.",
        "10-Minute Sunlight Break – Step outside, close your eyes, and feel the sun on your skin.",
        "Look at Happy Photos – Scroll through old photos that bring back happy memories.",
        "Self-Compassion Letter – Write a kind letter to yourself, as if comforting a friend.",
        "Holding a Weighted Object – Hug a pillow or weighted blanket for comfort.",
        "Watch a Funny Clip – Play a short funny video or meme to spark a smile.",
        "Sway to Music Slowly – Play a calming song and gently move your body.",
        "Mindful Walking – Take a slow walk, paying attention to your breathing and steps."
    ],
    "Anger/Resentment": [
        "Cooling Breath – Inhale through curled tongue, exhale through nose. Repeat 10 times.",
        "Tear Paper into Small Bits – Write your anger down, then tear the paper into tiny pieces.",
        "Hit a Pillow or Punch the Air – Safely release anger by hitting a pillow or air-boxing.",
        "Count Backward from 100 by 7s – Forces logical thinking, distracting from anger.",
        "Clench & Release Fists – Clench fists tight for 5 sec, then release, repeating 5 times.",
        "Fast 5-Minute Walk – Walk briskly to release pent-up frustration.",
        "Write an Angry Letter (Then Destroy It) – Write down your feelings, then shred or burn the letter safely.",
        "Hold Ice Cubes in Hands – The cold sensation calms anger quickly.",
        "Exhale Like a Lion’s Roar – Take a deep breath and exhale forcefully with an open mouth.",
        "Tense & Release Shoulders – Shrug up to your ears, hold for 5 sec, then release."
    ],
    "Happiness/Joy": [
        "Savor a Happy Memory for 60 Seconds – Close your eyes and relive a joyful moment.",
        "Dance to Your Favorite Song – Move your body freely to release feel-good endorphins.",
        "Stretch Arms Up & Smile – Changing posture can improve mood instantly.",
        "Write Down 3 Recent Wins – Acknowledge your small victories.",
        "Smell Something Pleasant – Inhale a favorite scent like citrus or lavender.",
        "Eat Something You Love Slowly – Mindful eating enhances the experience.",
        "Look at Bright Colors or a Sunset – Vibrant colors can lift your mood.",
        "Hug Yourself Firmly for 10 Seconds – Releases oxytocin, making you feel good.",
        "Watch a Comedy Skit – Laughter boosts immunity and happiness.",
        "Try a Small New Experience – Even trying a new flavor of tea sparks joy."
    ],
    "Disappointment/Regret": [
        "Reframe the Thought – Write one lesson learned from the experience.",
        "List Past Successes – Remind yourself of previous accomplishments.",
        "Write a Letter to Your Future Self – Offer encouragement and advice.",
        "Set a Small Goal – Achieve something simple to rebuild confidence.",
        "Shake Your Body for 30 Seconds – Helps release frustration physically.",
        "Mindful Coloring – Draw or color to distract and reset your focus.",
        "5-Minute Meditation on Acceptance – Sit still and accept the present moment.",
        "Write a \"Worst-Case Scenario\" & Counter It – Helps reframe negativity.",
        "Watch an Inspiring Talk – Motivates and uplifts perspective.",
        "Talk to Yourself Kindly – Replace negative self-talk with encouragement."
    ],
    "Shame/Guilt": [
        "Self-Compassion Exercise – Say: \“I am human, and mistakes help me grow.\”",
        "Write a Self-Forgiveness Letter – Address yourself kindly and express understanding.",
        "Guided Meditation on Self-Acceptance – Sit quietly and focus on accepting your imperfections.",
        "Draw a Representation of Your Shame – Express emotions visually through drawing.",
        "Talk to Yourself Like a Friend – Imagine what you would say to comfort a friend.",
        "Mirror Affirmations – Look in the mirror and say: \"I am enough.\"",
        "Write a \"Lessons Learned\" List – List things you have learned from mistakes.",
        "Tense & Release Your Hands – Helps release built-up guilt and tension.",
        "Watch a Video on Overcoming Perfectionism – Learn from experts about self-acceptance.",
        "Listen to Soothing Music Without Lyrics – Helps quiet self-criticism and promote relaxation."
    ],
    "Pride/Confidence": [
        "Power Pose for 2 Minutes – Stand confidently with hands on hips and chin up to boost self-assurance.",
        "List 3 Skills You Have Mastered – Reinforce self-trust by recognizing personal achievements.",
        "Repeat: “I am capable and strong.” – Use verbal affirmations to build confidence.",
        "Visualize a Past Success – Strengthen self-belief by recalling a moment of accomplishment.",
        "Take a 5-Minute Victory Walk – Walk with pride, as if celebrating a win.",
        "Journal One Thing You Did Well Today – Develop a habit of tracking small successes.",
        "Try a \"Yes, I Can\" Mantra – Repeat this phrase 10 times to reinforce self-efficacy.",
        "Set a Mini Goal & Achieve It – Accomplish a small task to boost confidence.",
        "Read or Watch an Inspiring Story – Draw motivation from stories of perseverance and success.",
        "Write a Letter to Your Future Self – Encourage yourself by acknowledging strengths and aspirations."
    ],
    "Comparison/Social Pressure": [
        "Digital Detox for 30 Minutes – Step away from social media to reduce comparison-driven anxiety.",
        "Affirmation: “I Am Enough” – Strengthen self-worth by affirming personal value.",
        "List 3 Strengths Unique to You – Focus on personal qualities that make you special.",
        "Turn Envy into Admiration – Shift perspective by learning from those you admire.",
        "Unfollow Triggers on Social Media – Remove content that negatively affects self-perception.",
        "Mindful Scrolling – Set a timer to use social media intentionally without overconsumption.",
        "Reframe a Comparison Thought – Replace negative comparisons with self-growth affirmations.",
        "List 3 Things You’ve Achieved Lately – Remind yourself of personal progress.",
        "Engage in a Hobby You Love – Redirect focus to enjoyable and fulfilling activities.",
        "Practice the \"Noticing Without Judgment\" Technique – Observe comparison thoughts without attaching emotions."
    ],
    "Empathy/Compassion": [
        "Loving-Kindness Meditation – Send kind thoughts to yourself and others to cultivate compassion.",
        "Set a Boundary with Kindness – Assert personal needs while maintaining respect for others.",
        "Write a Gratitude Letter to Someone – Express appreciation, even if the letter isn’t sent.",
        "Help Someone Anonymously – Perform a kind act without seeking recognition.",
        "Listen Deeply to Someone Without Responding – Practice active listening to build empathy.",
        "Visualize Walking in Someone Else’s Shoes – Imagine another’s perspective to enhance understanding.",
        "Pet or Hug Yourself – Use self-soothing techniques to generate warmth and comfort.",
        "Read a Short Story with Deep Emotion – Engage with narratives that foster empathy.",
        "Write Down What You Love About Someone – Focus on positive attributes to strengthen connections.",
        "Smile at a Stranger – Foster social connection through a simple, kind gesture."
    ],
    "Love/Trust Issues": [
        "Hand-on-Heart Exercise – Close your eyes, place your hand on your heart, and take deep breaths to cultivate self-compassion.",
        "Write: “What Do I Need to Feel Safe?” – Identify emotional needs to build trust in relationships.",
        "Listen to Calming Love Songs – Use music as a tool to soothe emotional wounds.",
        "Self-Love Affirmations – Repeat: \"I am worthy of love and trust\" to reinforce self-acceptance.",
        "Journaling to Release Pain – Write about emotions and experiences to process heartbreak.",
        "Draw a Symbol of Trust – Visually represent trust to redefine what it means to you.",
        "Give Yourself a Warm Hug – Use physical self-soothing techniques to promote emotional security.",
        "Slow Deep Breathing (10 Rounds) – Practice deep breathing to regulate emotional responses.",
        "Create a “What I Want in Love” List – Clarify personal relationship standards and desires.",
        "Do One Thing That Makes You Feel Loved – Engage in a comforting activity that brings joy and warmth."
    ],
    "Curiosity/Awe": [
        "Look at the Sky for 2 Minutes – Observe clouds or stars to experience a sense of wonder.",
        "Explore a Fun Fact – Read an interesting fact to stimulate curiosity.",
        "Try a “Beginner’s Mind” Exercise – Observe an everyday object as if seeing it for the first time.",
        "Stare at a Beautiful Photo or Artwork – Take in visual beauty to activate a sense of awe.",
        "Listen to an Instrumental Song You’ve Never Heard – Engage curiosity through unfamiliar music.",
        "Go for a Walk in a New Direction – Explore a new route to experience novelty and excitement.",
        "Ask a “What If?” Question – Think creatively about possibilities, such as time travel.",
        "Read a Random Wikipedia Page – Discover something new by exploring unexpected topics.",
        "Close Your Eyes & Touch an Object – Identify an object just by its texture to enhance sensory awareness.",
        "Write a Question You’d Love to Find the Answer To – Spark curiosity by formulating an intriguing question."
    ],
    "Belonging/Connection": [
        "Send a Message to Someone You Care About – Strengthen social bonds through communication.",
        "Write 3 Things You Like About Yourself – Boost self-acceptance and confidence.",
        "Look at an Old Group Photo & Reflect on Positive Moments – Recall happy memories to reinforce connection.",
        "Join an Online Forum or Community Related to Your Interests – Engage with like-minded individuals.",
        "Practice a 30-Second Smile at Yourself in the Mirror – Improve self-confidence and social ease.",
        "Listen to a Podcast About Human Stories – Feel connected through shared experiences.",
        "Give a Genuine Compliment to Someone – Encourage positive social interactions.",
        "Do a Random Act of Kindness – Perform a kind gesture to build a sense of belonging.",
        "Re-read a Meaningful Text Message from a Loved One – Reinforce emotional connection.",
        "Write Down “What Belonging Means to Me” – Define what belonging looks like in your life."
    ],
    "Nostalgia/Irony": [
        "Watch a Favorite Childhood Cartoon or Movie – Reconnect with joyful memories.",
        "Smell a Familiar Scent from Your Past – Use scent to trigger nostalgic memories.",
        "Flip Through an Old Photo Album – Reflect on past experiences and emotions.",
        "Write a Letter to Your Younger Self – Process past and present emotions through writing.",
        "Listen to a Song That Reminds You of a Specific Time – Experience emotional connections through music.",
        "Eat a Meal You Loved as a Kid – Reignite positive childhood associations through taste.",
        "Look at a Childhood Toy or Object (or Find an Image of It) – Spark warm memories of the past.",
        "Recall a Funny or Embarrassing Moment & Laugh About It – Embrace emotional growth through humor.",
        "Write Down a Lesson From Your Past That Still Guides You – Reflect on how past experiences have shaped you.",
        "Draw a Memory From Your Childhood – Express nostalgia creatively through art."
    ]
}

### 🔹 Generate Collaborative Filtering Dataset ###
def generate_cf_dataset():
    num_samples = 2000
    timestamps = [
        (datetime.now(timezone.utc) - timedelta(days=np.random.randint(0, 30))).isoformat()
        for _ in range(num_samples)
    ]

    cf_data = pd.DataFrame({
        'user_id': np.random.randint(100, 500, num_samples),
        'activity_id': np.random.choice(sum(activity_map.values(), []), num_samples),
        'rating': np.random.randint(3, 6, num_samples),  # Ratings between 3-5
        'timestamp': timestamps  # Added timestamps
    })

    cf_dataset_path = os.path.join(dataset_dir, "cf_training_data.csv")
    cf_data.to_csv(cf_dataset_path, index=False)
    print(f"Collaborative Filtering Dataset Created: {cf_dataset_path}")

    
### 🔹 Generate XGBoost Training Dataset ###
def generate_xgb_dataset():
    num_samples = 2000

    timestamps = [
        (datetime.now(timezone.utc) - timedelta(days=np.random.randint(0, 30))).isoformat()
        for _ in range(num_samples)
    ]
    
    xgb_data = [
        [
            np.random.randint(100, 500), 
            mood, 
            np.random.choice(activity_map[mood]), 
            np.random.choice(activity_map[mood]),
            timestamps[i]
        ]
        for i, mood in enumerate(np.random.choice(emotion_categories, num_samples))
    ]

    df_xgb = pd.DataFrame(xgb_data, columns=["user_id", "mood", "recent_activity", "suggested_activity", "timestamp"])
    xgb_dataset_path = os.path.join(dataset_dir, "xgb_training_data.csv")
    df_xgb.to_csv(xgb_dataset_path, index=False)
    print(f"XGBoost Training Dataset Created: {xgb_dataset_path}")

if __name__ == "__main__":
    print("🚀 Generating Datasets with Expert-Recommended Activities...")
    generate_cf_dataset()
    generate_xgb_dataset()
    print("All datasets successfully generated!")
