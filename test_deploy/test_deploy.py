"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


class State(rx.State):
    """The app state."""

    count: int = 0

    @rx.event
    def decrement(self):
        self.count -= 1

    @rx.event
    def increment(self):
        self.count += 1


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Deployment Succesfull!", size="9"),
            rx.hstack(
                rx.button("Decrement", on_click=State.decrement),
                rx.text(State.count, size="5"),
                rx.button("Increment", on_click=State.increment),
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.logo(),
    )


app = rx.App()
app.add_page(index)
