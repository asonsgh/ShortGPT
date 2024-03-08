import random

from shortGPT.config.api_db import ApiKeyManager, ApiProvider
from shortGPT.config.asset_db import AssetDatabase, AssetType
from shortGPT.engine.facts_short_engine import FactsShortEngine
from shortGPT.audio.eleven_voice_module import ElevenLabsVoiceModule
from shortGPT.config.languages import Language

# Set or get API Keys here
ApiKeyManager.set_api_key(ApiProvider.OPENAI, "")
ApiKeyManager.set_api_key(ApiProvider.ELEVEN_LABS, "")
ApiKeyManager.set_api_key(ApiProvider.PEXELS, "")

# Music and Video Links
music_links = [
    "https://www.youtube.com/watch?v=1WP_YLn1D1c",
    "https://www.youtube.com/watch?v=ZhECyz85FMc",
    "https://www.youtube.com/watch?v=6FNHe3kf8_s",
    "https://www.youtube.com/watch?v=p7ZsBPK656s",
    "https://www.youtube.com/watch?v=__CRWE-L45k",
    "https://www.youtube.com/watch?v=iaKgF1Vf5bQ"
]

video_links = [
    "https://www.youtube.com/watch?v=UJa80UPjREU",
    "https://www.youtube.com/watch?v=IWqqD3HXTp0",
    "https://www.youtube.com/watch?v=wgntRR5_Zvs",
    "https://www.youtube.com/watch?v=vLnX5JP4jVg",
    "https://www.youtube.com/watch?v=-qZqpM-k7sY",
    "https://www.youtube.com/watch?v=Lmb_G9klCvU"
]

# Choose random music and video
music_url = random.choice(music_links)
video_url = random.choice(video_links)

# Add assets to AssetDatabase
AssetDatabase.add_remote_asset("custom_music", AssetType.BACKGROUND_MUSIC, music_url)
AssetDatabase.add_remote_asset("custom_video", AssetType.BACKGROUND_VIDEO, video_url)

# Configure Voice Module
voice_module = ElevenLabsVoiceModule(api_key=ApiKeyManager.get_api_key(ApiProvider.ELEVEN_LABS), voiceName="Bella")

# Configure Content Engine
facts_type = "interesting_facts"  # Specify the type of facts you want
content_engine = FactsShortEngine(voiceModule=voice_module,
                                   facts_type=facts_type,
                                   background_video_name="custom_video",
                                   background_music_name="custom_music",
                                   num_images=4,
                                   language=Language.ENGLISH)

# Generate Content
for step_num, step_logs in content_engine.makeContent():
    print(f"{step_logs}")

# Get Video Output Path
print(content_engine.get_video_output_path())
