import urllib.request, os

base = r'C:\Users\gongjue\tiktok-reports\2026-04-09\yt_images'
os.makedirs(base, exist_ok=True)

videos = [
    ('01_strongest_streamer.jpg', '_JUlWtSCNbs'),
    ('02_beat.jpg', 'LifAnC8S4B0'),
    ('03_emotional_story.jpg', '38S-tywzIOw'),
    ('04_bts_dance.jpg', '4vD21i1UYqQ'),
    ('05_grape_bet.jpg', 'Pgpp-U3TtSo'),
    ('06_wing_man.jpg', 'dEYjnFCvpws'),
    ('07_horrible_histories.jpg', 'GTQCrZWLvm8'),
    ('08_illusion.jpg', 'hfSAbl-KnAo'),
    ('09_relatable_comedy.jpg', 'X8Rl-ZhAJA0'),
    ('10_unicorn_ball.jpg', 'SXu0wrf0qAk'),
]

for fname, vid in videos:
    url = f'https://i.ytimg.com/vi/{vid}/maxresdefault.jpg'
    path = os.path.join(base, fname)
    try:
        urllib.request.urlretrieve(url, path)
        size = os.path.getsize(path)
        print(f'OK: {fname} ({size} bytes)')
    except Exception as e:
        url2 = f'https://i.ytimg.com/vi/{vid}/sddefault.jpg'
        try:
            urllib.request.urlretrieve(url2, path)
            size = os.path.getsize(path)
            print(f'OK (sd fallback): {fname} ({size} bytes)')
        except Exception as e2:
            print(f'FAIL: {fname} - {e2}')

print('Done!')
