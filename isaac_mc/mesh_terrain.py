from random import randrange
from ursina import *

class MeshTerrain:

    def __init__(this):

        this.block = load_model('block.obj')
        this.textureAtlas = 'texture_atlas_3.png'

        this.subsets = []
        this.numSubsets = 1
        this.subWidth = 32

        for i in range(0,this.numSubsets):
            e = Entity( model=Mesh(),
                        texture=this.textureAtlas)
            e.texture_scale*=64/e.texture.width
            this.subsets.append(e)


    def genBlock(this,x,y,z):
        # Extend or add to vertices of our model.
        model = this.subsets[0].model

        model.vertices.extend([ Vec3(x,y,z) + v for v in
                                this.block.vertices])

        # This is the texture atlas co-ord for grass :)
        uu = 8
        uv = 7
        model.uvs.extend([Vec2(uu,uv) + u for u in this.block.uvs])


    def genTerrain(this):

        x = 0
        z = 0
        y = randrange(-1,1)

        d = int(this.subWidth*0.5)

        for k in range(-d,d):
            for j in range(-d,d):

                this.genBlock(x+k,y,z+j)

            this.subsets[0].model.generate()