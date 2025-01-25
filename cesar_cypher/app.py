import flet as ft
import cesar as cs
def main(page: ft.Page):
    def chiffrer_message(e):
        message = e.control.value
        message_majuscule = cs.lettres_majuscules(message)
        t.value = cs.chiffrer_cesar(message_majuscule, int(decalage.value))
        page.update()

    def dechiffrer_message(e):
        message = e.control.value
        message_majuscule = cs.lettres_majuscules(message)
        t2.value = cs.dechiffrer_cesar(message_majuscule, int(decalage2.value))
        page.update()

    t = ft.Text()
    tb = ft.TextField(
        label="Entrer votre message à chiffrer",
        on_change=chiffrer_message,
    )
    decalage = ft.TextField(
        label="Entrer le décalage",
    )
    tb2 = ft.TextField(
        label="Entrer votre message à déchiffrer",
        on_change=dechiffrer_message,
    )
    t2 = ft.Text()

    decalage2 = ft.TextField(
        label="Entrer le décalage",
    )

    page.add(decalage,tb,t, decalage2,tb2, t2)

ft.app(main)
