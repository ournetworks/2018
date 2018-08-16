Our Networks Livestreaming Retrospective
========================================

Attendees:
- @benhylau
- @darkdrgn2k
- @elon
- @dcwalk
- @hank (missed call, thoughts added in post)

# Round of Debrief 

## Planning

- dd: little ramp up time (Wed walkthru to Sat)
- dd: unable to test interface (audio problems as a result) and macgyver'd cables
- dd: OpenVPN modifications to be more resilient? RTMP stream a single point of failure. Dropped packets messing up (OpenVPN over TCP to ensure no dropped packets in the RTMP stream)
- dd: RTMP server pushed to to, this might also be a constraint for many other issues?
- b: lots of exploration on what is possible, didn't have predefined goals, requirements were: reliable, streams over ipfs and http, gateways and ipns <-- initial goal
    - stretched into: embeddable player, etc...
    - better communication about goals across ON team + streaming crew
- b: things still in pieces until the shipping date, different expectations of "ready" and a product "to ship," e.g., assets OBS, provisioning (terraform, manual cluster) 
- b: documentation needs to be improved, etc... other process components learned thru deployment
- b: friction points between ON + livestreaming team staying in/out of sync?
- dd: no defined roles (A/V side?), at times too many chefs?
- dc: need mitigation plan of not having access to venue
- dc: difficult to figure out progress by Our Networks organizer team
- dc: publish an equipment list that includes the little things we needed the day of (like a camping packing list for next year)
- dc: too early to say, but we may end up rolling more of our own equipment

## Day of

- dd: day of-- don't touch stuff that works (benhylau: +1)
- dd: problem with audio sync, couldn't fix. still unsure why. think a mix of given setup (video/audio encoding)
- dd: overall pretty solid given constraints, staff/volunteer levels
- dd: saw link go down once, quick restart and stuff came back up
- dd: inexplicable size bump (chunks doubling in size for no apparent reason) _still confusing_ but didn't seem to impact quality
- dd: thow mic wierdness, prompts to presenters about distance from mic
- b: figuring out in advance who wants to be streamed in advance versus not
    - dc: there will likely be some flux day of so it was great to be flex
    - dd: didn't prepare screens 
    - dc: this might be attributable to the out-of-sync of comms.. was discussed
- dd: player feedback... wasn't clear from **interface** that the stream worked in browser (and no additional software needed)
- b: how IPFS is being used a blackbox?
- dd: lack of advertising that there was a livestream?
- b: play music in venue!
- hw: Venue music should be (and eventually was) handled by a different system / computer
- dd+b: day-of anarchy
- dc: better day-of communication
- b: need to agree on one place where we note whether a talk is streamed, audio-only, recorded, or not at all, and have one dedicated time and person to discuss this with speaker, other people just reference this source of global truth instead of asking the speaker repeatedly
- dd: PNP for slides in OBS cut off some text

# Distinct issues

## Sync

- dd: encoders not designed for what what happening (stream + mixer board), were there alternative set ups that would have addressed this?
    - tried to feed audio to encoder, didn't work (potential?)
- dd: hacky setup with location, we got lucky
- hw: Yes, the audio and video must be in sync before they hit the encoder.  Our setup had HD-SDI video being encoded to digital and then sent to the capture card over HDMI.  The audio was fully analog until it hit Elon's laptop.  Both audio and video streams must be processed as analog signals and then sent to a single capture device where they are encoded at the same time.  This way there will be no delay!

## RTMP and/or FFMPEG

- need RTMP to push non-IPFS
- OBS configuring chunks hinky
- b: integration with ffmpeg?
    - dd: way to scrap completely? fragmenting issues? something about a nginx plugin for HLS... _but_ ffmpeg handles multiple devices?

## Race condition on m3u8 file

- some loop and exit in script, but after ffmpeg writes chunk then creates file. There is a gap there that could cause a race condition

# TODO

- file bugs on github (i.e., including ffmpeg, m3u8, etc.... mentioned above)
- dc: request: make a "camping list"
- hw: stream video editing ;P (I've started it!)

# Hopes and Dreams

- multiple rooms?
- p2p chat (as a spin off)
- closed captioning
- over our mesh network
- hw: Dedicated room tone microphone
- dc: week long set up a/v network as site build out (get grant g.) to teach folks in tomesh (and toronto?) interested in learning this stuff. Crimping workshop included
    - camp-style: hacking at HAR, magnetic field, chaos camp
- dc: beautiful documentation!
- IPNS and `ipfs pin add`
- peerpad / chat integration (for discussion and Q&A?)
- better accomodation for remote speakers (look at chaos model)
- a/v hardware purchased?
    - dc: we need to understand who will own it after!
- as a service for other conferences?
- help Ryan build this at FreeGeek
