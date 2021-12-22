"""
* -------------------------------------------------------------------------------- *
* "THE BEER-WARE LICENSE" (Revision 42):                                           *
* <thornale1@gmail.com> wrote this file.  As long as you retain this notice you    *
* can do whatever you want with this stuff. If we meet some day, and you think     *
* this stuff is worth it, you can buy me a beer in return.             thorn_ale   *
* -------------------------------------------------------------------------------- *
"""


import numpy as np
import sys
import cv2
import time


def main(renderer_type):
    """Take a video feed and convert it to ascii in the terminal

    Args:
        renderer_type (str): argument sent through the command-line to set the type of renderding
            - 16 select the 16 char renderer
            - 64 select the 64 char renderer
    """
    # clear stdout buffer
    sys.stdout.buffer.write(b'\033c')

    # start video capture from device 0
    vid = cv2.VideoCapture(0)
    rendered_frame = None

    # You must chose between a 16 char rendering and a 64 char rendering
    discrete_range = {
        '16': [x*16 for x in range(1, 17)],
        '64': [x*4 for x in range(1, 65)]
    }[renderer_type]
    charset = {
        '16': ' .-=+oO0HXS$8&#@',
        '64': ' .\'`^",:;Il!i><~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZkhao*#MW&8%B@$'
    }[renderer_type]

    while(True):
        try:
            if rendered_frame:
                # write bytes directly to stdout buffer to shave off some ms
                # See https://docs.microsoft.com/en-us/windows/console/console-virtual-terminal-sequences for details about control sequences on windows terminal
                # b'\x1b[0;0H' => set the cursor at the (0;0) position of the terminal (if you want a smooth feed you must not clear the screen betwen each frames)
                # b'\x1b[32m' => set the foreground (i.e the text) to be green (use b'\x1b[38;2;R;G;Bm' to set a custom color but not all windows terminals accept it)
                sys.stdout.buffer.write(
                    b'\x1b[0;0H' + b'\x1b[32m' + ('\n'.join(rendered_frame)).encode('utf-8'))

            # get frame from camera
            _, frame = vid.read()

            # flip the image
            frame = cv2.flip(frame, 1)

            # get it as a grey scale array
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # resize the image to match your terminal size
            frame = cv2.resize(frame, (160, 50))

            # transform all grey scale values to a discrete range [0-15] or [0-63] given renderer_type
            frame = np.digitize(frame, discrete_range)

            # associate all discrete values to the corresponding ascii char
            ascii_frame = np.vectorize(lambda x: charset[x])(frame)

            # render the new frame
            rendered_frame = [''.join(x) for x in ascii_frame]

            # cap at 60 FPS
            time.sleep(1/60)

        # if we catch the exit sequence (CTRL+C) we break the loop
        except KeyboardInterrupt:
            break

    # reset the terminal style
    sys.stdout.buffer.write(b'\x1b[0m')

    # open-CV closing sequence
    vid.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main(sys.argv[1])
