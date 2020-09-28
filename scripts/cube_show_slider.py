def cube_show_slider(cube, axis=2, **kwargs):
    """
    Display a 3d ndarray with a slider to move along the third dimension.

    Extra keyword arguments are passed to imshow
    """
    import matplotlib.pyplot as plt
    from matplotlib.widgets import Slider, Button, RadioButtons

    # check dim
    if not cube.ndim == 3:
        raise ValueError("cube should be an ndarray with ndim == 3")

    # generate figure
    fig = plt.figure()
    ax = plt.subplot(111)
    fig.subplots_adjust(left=0.05, bottom=0.15)

    # select first image
    s = [slice(0, 1) if i == axis else slice(None) for i in range(3)]
    im = cube[s].squeeze()

    # display image
    l = ax.imshow(im, **kwargs)
    fig.colorbar(l)

    # define slider
    axcolor = 'lightgoldenrodyellow'
    ax = fig.add_axes([0.18, 0.05, 0.58, 0.03], facecolor=axcolor)

    slider = Slider(ax, 'Slice index', 0, cube.shape[axis] - 1,
                    valinit=0, valfmt='%i')

    def update(val):
        ind = int(slider.val)
        s = [slice(ind, ind + 1) if i == axis else slice(None)
                 for i in range(3)]
        im = cube[s].squeeze()
        #l.set_data(im, **kwargs)
        l.set_data(im)
        fig.canvas.draw()

    slider.on_changed(update)

    plt.show()
