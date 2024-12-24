import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt

def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    nyquist = 0.5 * fs
    low = lowcut / nyquist
    high = highcut / nyquist
    b, a = butter(order, [low, high], btype='band')
    return filtfilt(b, a, data)

def process_frame(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    signal_resp = np.mean(gray)
    signal_rppg = np.std(gray)
    return signal_resp, signal_rppg

def release_resources(cap):
    """
    Fungsi untuk memastikan semua sumber daya dirilis.
    """
    if cap.isOpened():
        cap.release()
    cv2.destroyAllWindows()
    print("Sumber daya kamera dan jendela sudah dirilis.")

def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Tidak dapat membuka webcam.")
        return

    print("Tekan 'q' untuk keluar.")
    
    respiration_signals = []
    rppg_signals = []
    timestamps = []

    fs = 30.0
    plt.ion()
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6))
    line1, = ax1.plot([], [], label='Sinyal Respirasi', color='b')
    line2, = ax2.plot([], [], label='Sinyal rPPG', color='g')

    ax1.set_xlim(0, 10)
    ax2.set_xlim(0, 10)
    ax1.set_ylim(0, 255)
    ax2.set_ylim(0, 255)
    ax1.set_xlabel('Waktu (detik)')
    ax2.set_xlabel('Waktu (detik)')
    ax1.set_ylabel('Intensitas')
    ax2.set_ylabel('Intensitas')
    ax1.legend()
    ax2.legend()

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Error: Tidak dapat membaca frame.")
                break
            
            resp_signal, rppg_signal = process_frame(frame)
            respiration_signals.append(resp_signal)
            rppg_signals.append(rppg_signal)
            timestamps.append(len(timestamps) / fs)

            if len(timestamps) > fs * 10:
                respiration_signals = respiration_signals[-int(fs * 10):]
                rppg_signals = rppg_signals[-int(fs * 10):]
                timestamps = timestamps[-int(fs * 10):]

            line1.set_data(timestamps, respiration_signals)
            line2.set_data(timestamps, rppg_signals)
            ax1.set_xlim(timestamps[0], timestamps[-1])
            ax2.set_xlim(timestamps[0], timestamps[-1])
            fig.canvas.draw()
            fig.canvas.flush_events()
            
            cv2.imshow("Webcam", frame)
            
            key = cv2.waitKey(1)
            if key & 0xFF == ord('q'):
                print("Menutup program atas permintaan pengguna...")
                break

    except Exception as e:
        print(f"Terjadi error: {e}")

    finally:
        # Pastikan semua sumber daya dirilis
        release_resources(cap)
        plt.ioff()
        plt.show()
        print("Kamera dirilis dan jendela ditutup.")

if __name__ == "__main__":
    main()
