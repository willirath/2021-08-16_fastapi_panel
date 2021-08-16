import panel as pn
import pandas as pd

pn.extension()


def get_pi(n=10):
    pi = pd.read_json(f"http://compute/pi/?length={n}", typ="series")["pi"]
    return float(pi)


bootstrap = pn.template.BootstrapTemplate(title="Estimate PI")

bootstrap.main.append(
    pn.Row(
        pn.Card(
            pn.interact(
                get_pi,
                n=[1, 10, 100, 1_000, 10_000],
            ),
            title="PI from an n rand points",
        ),
    )
)
bootstrap.servable()