import facemorpher

WIDTH, HEIGHT = 1024, 1024


def morph(image1_path, image2_path, output_path):
    facemorpher.averager(
        [image1_path, image2_path],
        out_filename=output_path,
        plot=False,
        width=WIDTH,
        height=HEIGHT,
        blur_edges=True,
        background='transparent',
    )
