from manim import *
import os, inspect


class laggingUpdater(Scene):
    def construct(self):
        vt = ValueTracker(0)
        dot1a = Dot().shift(3 * UP)
        dot2a = Dot().shift(3 * UP)

        def updater(mobj):
            mobj.set_x(vt.get_value())

        dot1a.add_updater(updater)
        dot2a.add_updater(updater)

        print(
            f"\n\n\nCalling self.play(LaggedStart): Caller [{os.path.basename(inspect.currentframe().f_back.f_code.co_filename)}:{inspect.currentframe().f_back.f_lineno}] Callee [{os.path.basename(__file__)}:{inspect.currentframe().f_lineno}]"
        )
        self.play(
            LaggedStart(
                Create(
                    dot1a,
                ),
                Create(
                    dot2a,
                ),
                # introducer=True,
            )
        )
        print(
            f"Returning from self.play(LaggedStart): Caller [{os.path.basename(inspect.currentframe().f_back.f_code.co_filename)}:{inspect.currentframe().f_back.f_lineno}] Callee [{os.path.basename(__file__)}:{inspect.currentframe().f_lineno}]",
            "\n\n\n",
        )

        # print(
        #     f"\n\n\nCalling dot1a.resume_updating(): Caller [{os.path.basename(inspect.currentframe().f_back.f_code.co_filename)}:{inspect.currentframe().f_back.f_lineno}] Callee [{os.path.basename(__file__)}:{inspect.currentframe().f_lineno}]"
        # )
        # dot1a.resume_updating()

        # print(
        #     f"Returning from dot1a.resume_updating(): Caller [{os.path.basename(inspect.currentframe().f_back.f_code.co_filename)}:{inspect.currentframe().f_back.f_lineno}] Callee [{os.path.basename(__file__)}:{inspect.currentframe().f_lineno}]"
        # )
        self.wait()
        self.play(vt.animate.set_value(7), run_time=4)
        self.wait()

        print(
            f"\n\n\nCalling self.play(): Caller [{os.path.basename(inspect.currentframe().f_back.f_code.co_filename)}:{inspect.currentframe().f_back.f_lineno}] Callee [{os.path.basename(__file__)}:{inspect.currentframe().f_lineno}]"
        )

        self.play(vt.animate.set_value(0), run_time=2)
        print(
            f"Returning from self.play: Caller [{os.path.basename(inspect.currentframe().f_back.f_code.co_filename)}:{inspect.currentframe().f_back.f_lineno}] Callee [{os.path.basename(__file__)}:{inspect.currentframe().f_lineno}]"
        )
        self.wait()


laggingUpdater().render(preview=True)
