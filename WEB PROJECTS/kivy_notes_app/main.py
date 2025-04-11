from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.list import TwoLineListItem
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from database import NotesDatabase

class NotesApp(MDApp):
    def build(self):
        self.db = NotesDatabase()
        return Builder.load_file("notes.kv")

    def on_start(self):
        self.load_notes()

    def load_notes(self):
        notes = self.db.get_notes()
        notes_list = self.root.ids.notes_list
        notes_list.clear_widgets()

        for note in notes:
            item = TwoLineListItem(text=note[1], secondary_text=note[2], on_release=lambda x, nid=note[0]: self.delete_note_dialog(nid))
            notes_list.add_widget(item)

    def add_note_dialog(self):
        self.dialog = MDDialog(
            title="Add Note",
            type="custom",
            content_cls=MDTextField(hint_text="Title"),
            buttons=[
                MDRaisedButton(text="CANCEL", on_release=lambda x: self.dialog.dismiss()),
                MDRaisedButton(text="ADD", on_release=self.add_note)
            ]
        )
        self.dialog.open()

    def add_note(self, *args):
        title = self.dialog.content_cls.text
        if title:
            self.db.add_note(title, "Tap to edit")
            self.dialog.dismiss()
            self.load_notes()

    def delete_note_dialog(self, note_id):
        self.dialog = MDDialog(
            title="Delete Note?",
            buttons=[
                MDRaisedButton(text="CANCEL", on_release=lambda x: self.dialog.dismiss()),
                MDRaisedButton(text="DELETE", on_release=lambda x: self.delete_note(note_id))
            ]
        )
        self.dialog.open()

    def delete_note(self, note_id):
        self.db.delete_note(note_id)
        self.dialog.dismiss()
        self.load_notes()

    def on_stop(self):
        self.db.close()

if __name__ == "__main__":
    NotesApp().run()
