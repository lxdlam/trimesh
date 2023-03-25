try:
    from . import generic as g
except BaseException:
    import generic as g


class ViewerTest(g.unittest.TestCase):

    def test_viewer(self):
        try:
            from pyglet import gl
        except BaseException:
            return

        # make a sphere
        mesh = g.trimesh.creation.icosphere()

        # get a scene object containing the mesh, this is equivalent to:
        # scene = trimesh.scene.Scene(mesh)
        scene = mesh.scene()

        # set a GL config that fixes a depth buffer issue in xvfb
        window_conf = gl.Config(double_buffer=True, depth_size=24)
        # run the actual render call
        png = scene.save_image(resolution=[1920, 1080],
                               window_conf=window_conf)

        assert len(png) > 0

        
if __name__ == '__main__':
    g.trimesh.util.attach_to_log()
    g.unittest.main()
