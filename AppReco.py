import speech_recognition as sr
import time
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class VoiceRecognitionApp(App):

    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.label = Label(text='Parlez maintenant...')
        layout.add_widget(self.label)

        self.grid_layout = GridLayout(cols=5, rows=5, size_hint=(1, 0.9))
        self.grid_layout.spacing = [5,5]

        for i in range(25):
            self.grid_layout.add_widget(Button(text='', font_size=50))

        layout.add_widget(self.grid_layout)

        self.col_labels = BoxLayout(orientation='horizontal', size_hint=(1, 0.1))
        for i in range(1, 6):
            self.col_labels.add_widget(Label(text=str(i), font_size=30, size_hint=(1/5, 1)))
        layout.add_widget(self.col_labels)

        return layout

    def on_start(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source)

        self.stop_listening = self.recognizer.listen_in_background(self.microphone, self.callback)

    def on_stop(self):
        self.stop_listening()

    def callback(self, recognizer, audio):
        try:
            ordre = recognizer.recognize_google(audio, language='fr-FR')
            if ordre == "colonne 1" or ordre == "première colonne" or ordre == "1e colonne":
                self.allumer_case(4, ordre)
                time.sleep(2)
                self.label.text = "Parlez maintenant..."
            elif ordre == "colonne 2" or ordre == "deuxième colonne" or ordre == "2e colonne":
                self.allumer_case(3, ordre)
                time.sleep(2)
                self.label.text = "Parlez maintenant..."
            elif ordre == "colonne 3" or ordre == "troisième colonne" or ordre == "3e colonne":
                self.allumer_case(2, ordre)
                time.sleep(2)
                self.label.text = "Parlez maintenant..."
            elif ordre == "colonne 4" or ordre == "quatrième colonne" or ordre == "4e colonne":
                self.allumer_case(1, ordre)
                time.sleep(2)
                self.label.text = "Parlez maintenant..."
            elif ordre == "colonne 5" or ordre == "cinquième colonne" or ordre == "5e colonne":
                self.allumer_case(0, ordre)
                time.sleep(2)
                self.label.text = "Parlez maintenant..."
            elif ordre == "quitter":
                self.stop_listening()
                self.label.text = "Au revoir !"
                App.get_running_app().stop()
            else:
                self.label.text = "Je n'ai pas compris, veuillez réessayer..."
        except sr.UnknownValueError:
            self.label.text = "Je n'ai pas compris, veuillez réessayer..."
        except sr.RequestError as e:
            self.label.text = "Impossible de contacter le service de reconnaissance vocale ({0})".format(e)

    def allumer_case(self, colonne, ordre):
        for i in range(0,5):
            button = self.grid_layout.children[i * 5 + colonne]
            if button.text == '':
                button.background_color = [70,250,0,0.8]
                button.text = 'X'
                self.label.text = "Je mets la balle dans la " + ordre
                return
        self.label.text = "La "+ordre+ " est pleine, veuillez en choisir une autre."

if __name__ == '__main__':
    VoiceRecognitionApp().run()
