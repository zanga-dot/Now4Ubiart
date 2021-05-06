import json

with open("input.json") as f:
    inputt=json.load(f)

ktape={
"__class": "Tape",
"Clips": [],
"TapeClock": 0,
"TapeBarCount": 1,
"FreeResourcesAfterPlay": 0,
"MapName": inputt["MapName"],
"SoundwichEvent": ""
}

idd=1
for lyric in inputt["lyrics"]:
    index=0
    while(index<len(inputt["beats"])):
        if(lyric["time"]>inputt["beats"][index]):
            division=(inputt["beats"][index+1]-inputt["beats"][index])/24
            break
        index+=1
    ktape["Clips"].append({
    "__class": "KaraokeClip",
    "Id": idd,
    "TrackId": 0,
    "IsActive": 1,
    "StartTime": int(lyric["time"]/division),
    "Duration": int(lyric["duration"]/division),
    "Pitch": 8.661958,
    "Lyrics": lyric["text"],
    "IsEndOfLine": lyric["isLineEnding"],
    "ContentType": 1,
    "StartTimeTolerance": 4,
    "EndTimeTolerance": 4,
    "SemitoneTolerance": 5
    })
    idd+=1

dtape={
"__class": "Tape",
"Clips": [],
"TapeClock": 0,
"TapeBarCount": 1,
"FreeResourcesAfterPlay": 0,
"MapName": inputt["MapName"],
"SoundwichEvent": ""
}

for picto in inputt["pictos"]:
    index=0
    while(index<len(inputt["beats"])):
        if(picto["time"]>inputt["beats"][index]):
            division=(inputt["beats"][index+1]-inputt["beats"][index])/24
            break
        index+=1
    dtape["Clips"].append({
    "__class": "PictogramClip",
    "Id": idd,
    "TrackId": 575629419,
    "IsActive": 1,
    "StartTime": int(picto["time"]/division),
    "Duration": int(picto["duration"]/division),
    "PictoPath": "world/maps/"+inputt["MapName"].lower()+"/timeline/pictos/"+picto["name"]+".png",
    "CoachCount": 4294967295
    })
    idd+=1

with open("moves0.json") as f:
    moves0=json.load(f)

with open("moves1.json") as f:
    moves1=json.load(f)

with open("moves2.json") as f:
    moves2=json.load(f)

with open("moves3.json") as f:
    moves3=json.load(f)

coachid=0
for moves in [moves0,moves1,moves2,moves3]:
    for move in moves:
        index=0
        while(index<len(inputt["beats"])):
            if(move["time"]>inputt["beats"][index]):
                division=(inputt["beats"][index+1]-inputt["beats"][index])/24
                break
            index+=1
        try:
            goldmove=move["GoldMove"]
        except Exception:
            goldmove=0
        dtape["Clips"].append({
        "__class": "MotionClip",
        "Id": idd,
        "TrackId": 4094799440,
        "IsActive": 1,
        "StartTime": int(move["time"]/division),
        "Duration": int(move["duration"]/division),
        "ClassifierPath": "world/maps/"+inputt["MapName"].lower()+"/timeline/pictos/"+move["name"]+".msm",
        "GoldMove": goldmove,
        "CoachId": coachid,
        "MoveType": 0,
        "Color": [1, 0.572549, 0.937255, 0.309804],
        "MotionPlatformSpecifics": {
        "X360": {
        "__class": "MotionPlatformSpecific",
        "ScoreScale": 1,
        "ScoreSmoothing": 0,
        "LowThreshold": 0.200000,
        "HighThreshold": 1
        },
        "ORBIS": {
        "__class": "MotionPlatformSpecific",
        "ScoreScale": 1,
        "ScoreSmoothing": 0,
        "LowThreshold": -0.200000,
        "HighThreshold": 0.600000
        },
        "DURANGO": {
        "__class": "MotionPlatformSpecific",
        "ScoreScale": 1,
        "ScoreSmoothing": 0,
        "LowThreshold": 0.200000,
        "HighThreshold": 1
        }
        }
        })
        idd+=1
    coachid+=1

musictrack={
"__class": "Actor_Template",
"WIP": 0,
"LOWUPDATE": 0,
"UPDATE_LAYER": 0,
"PROCEDURAL": 0,
"STARTPAUSED": 0,
"FORCEISENVIRONMENT": 0,
"COMPONENTS": [{
"__class": "MusicTrackComponent_Template",
"trackData": {
"__class": "MusicTrackData",
"structure": {
"__class": "MusicTrackStructure",
"markers": list(map(lambda x: int(x*48),inputt["beats"])),
"signatures": [{
"__class": "MusicSignature",
"marker": 8,
"beats": 4
}
],
"sections": [{
"__class": "MusicSection",
"marker": 16,
"sectionType": 8,
"comment": ""
}
],
"startBeat": 0,
"endBeat": len(inputt["beats"]),
"videoStartTime": 0,
"previewEntry": int(len(inputt["beats"])/2),
"previewLoopStart": int(len(inputt["beats"])/2),
"previewLoopEnd": len(inputt["beats"]),
"volume": 0
},
"path": "world/maps/"+inputt["MapName"].lower()+"/audio/"+inputt["MapName"].lower()+".wav",
"url": "jmcs://jd-contents/"+inputt["MapName"]+"/"+inputt["MapName"]+".ogg"
}
}
]
}

json.dump(dtape,open("output/"+inputt["MapName"].lower()+"_tml_dance.dtape.ckd","w"))
json.dump(ktape,open("output/"+inputt["MapName"].lower()+"_tml_karaoke.ktape.ckd","w"))
json.dump(musictrack,open("output/"+inputt["MapName"].lower()+"_musictrack.tpl.ckd","w"))