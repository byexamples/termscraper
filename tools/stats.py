import io
import os.path
import sys

import termscraper


if __name__ == "__main__":
    benchmark = os.environ["BENCHMARK"]
    lines, columns = map(int, os.environ.get("GEOMETRY", "24x80").split('x'))
    optimize_conf = int(os.environ.get("OPTIMIZECONF", "0"))
    sys.argv.extend(["--inherit-environ", "BENCHMARK,GEOMETRY,OPTIMIZECONF"])

    with io.open(benchmark, "rb") as handle:
        data = handle.read()

    extra_args = {}
    if optimize_conf:
        extra_args = {
                'track_dirty_lines': False,
                'styleless': True,
                }

    screen = termscraper.Screen(columns, lines, **extra_args)
    stream = termscraper.Stream(screen, trace_callbacks=True)

    stream.feed_binary(data)

    print("Terminal input:", os.path.basename(benchmark))
    print("Stream stats:")
    print(stream.stats(reset=True))
    print()

    print("Screen stats:")
    print(screen.stats())


