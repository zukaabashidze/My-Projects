import speech_recognition as sr # xmis gasagebad
import time # current time gasagebad
from PIL import ImageGrab # image capturing isatvis
import cv2 # videos gaadasagebad (frame clipping type shi')
import numpy as np # aseve videostvis
import threading # threading rata vakontrolot videos ighebs tuara sanamde vakontrolebt stop vitkvit tuara (orivem ertad ro imushaos)
from win10toast import ToastNotifier # notification ebistvis
import os #directory shesakmnelad


#directory ebs ezebs screenshot,video ebis da tuar aris qmnis rata sheinaxos gadaghebuli videoebi da screenshotebi
def create_directories():
    base_dir = os.getcwd()
    screenshot_folder = os.path.join(base_dir, "screenshots")
    video_folder = os.path.join(base_dir, "videos")
    if not os.path.exists(screenshot_folder):
        os.makedirs(screenshot_folder)
        print(f"Created folder: {screenshot_folder}")
    if not os.path.exists(video_folder):
        os.makedirs(video_folder)
        print(f"Created folder: {video_folder}")
    return screenshot_folder, video_folder

screenshot_folder, video_folder = create_directories()


# Global variablebi shesamowmeblad tu videos vighebt an thread midis (videos gadagheba)
stop_recording = False
recording_thread = None  

#videos gadagheba.. savedeba axlandeli drois saxelit rata videoebi ertmanets ar gadaeweros
def videogadagheba():
    global stop_recording

    timestamp = time.strftime("%Y-%m-%d-%H-%M-%S")
    output_filename = os.path.join(video_folder,f'screen_record_{timestamp}.mp4')

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    screen_width = 1920
    screen_height = 1080
    frame_rate = 20.0
    out = cv2.VideoWriter(output_filename, fourcc, frame_rate, (screen_width, screen_height))

    print("vigheb videos tkvi 'stop' shesachereblad..")
    while not stop_recording:
        # screenis capturing
        screenshot = ImageGrab.grab(bbox=(0, 0, screen_width, screen_height))
        frame = np.array(screenshot)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        out.write(frame)

    # dasaveba sabolood roca stop_recording variable True gaxdeba
    out.release()
    cv2.destroyAllWindows()
    print(f"sheinaxa video aq: {output_filename}")

#screenshot gadagheba aris gaketebuli
def gadagheba():
    timestamp = time.strftime("%Y-%m-%d-%H-%M-%S")
    filename = os.path.join(screenshot_folder,f"screenshot_of_{timestamp}.png")
    screenshot = ImageGrab.grab()
    screenshot.save(filename)
    print(f"sheinaxa video aq: {filename}")

#xmis gageba da chawera
def chasaweri(recognizer, microphone):
    try:
        with microphone as source:
            print("gisment...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
        return recognizer.recognize_google(audio).lower()
    except sr.UnknownValueError:
        return None
    except sr.WaitTimeoutError:
        print("xma ver gaigona timeout periodisas...")
        return None

#xmis mosmena da commandebis gageba ,amushaveba
def voice_listener(recognizer, microphone):
    global stop_recording, recording_thread
    toast = ToastNotifier()

    while True:
        command = chasaweri(recognizer, microphone)
        if command:
            print(f"command icno: {command}")
            #tu command udris 'record'-s arecordebs
            if "record" in command or "start recording" in command:
                if recording_thread and recording_thread.is_alive():
                    toast.show_toast("Error", "ukve record mimdinareobs", duration=4)
                else:
                    toast.show_toast("Screen Recorder", "Recording daiwyo... tkvi 'stop'rom gacherdes..", duration=4)
                    stop_recording = False
                    recording_thread = threading.Thread(target=videogadagheba)
                    recording_thread.start()
            #tu command udris 'stop'-s acherebs records
            elif "stop" in command:
                if recording_thread and recording_thread.is_alive():
                    stop_recording = True
                    recording_thread.join()  # Wait for the thread to finish
                    toast.show_toast("Screen Recorder", "recording gacherda..", duration=4)
                else:
                    toast.show_toast("Error", "recording ar mimdinareobs verafer gavacherebt...", duration=4)
            #tu command udris 'screenshots'-s ighebs screenshot-s
            elif "screenshot" in command or "take a screenshot" in command:
                toast.show_toast("Screenshot", "screenshot gadaigho..", duration=4)
                gadagheba()
            #tu open udris commands  shemdeg moyolil sitkvas(aplikaciis saxels) ezebs pc-shi da xsnis tu ipova
            elif "open" in command:
               new_command =  command.split()
               new_command.remove("open")
            #tu open udris commands  shemdeg moyolil sitkvas(aplikaciis saxels) ezebs pc-shi da tishavs tu ipova rom gaxsnilia
            elif "close" in command:
               new_command =  command.split()
               new_command.remove("close")
            else:
                toast.show_toast("amocunobi command", "scade 'record', 'stop', or 'screenshot'.", duration=4)

#mtavari kodi
if __name__ == "__main__":
    #declaration speech recognition variablebis
    r = sr.Recognizer()
    mic = sr.Microphone()
    r.energy_threshold = 400
    #gashveba mtavari funkciis
    voice_listener(r, mic)