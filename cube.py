import random

class Cube:
    def __init__(self):
        """
        WHITE FACE = TOP FACE
        RED FACE = FRONT FACE
        BLUE FACE = RIGHT FACE
        GREEN FACE = LEFT FACE
        ORANGE FACE = LEFT FACE
        YELLOW FACE = BOTTOM FACE
        """
        self.cube = [
            [
                ['w', 'w', 'w'],
                ['w', 'w', 'w'],
                ['w', 'w', 'w']
            ],
            [
                ['r', 'r', 'r'],
                ['r', 'r', 'r'],
                ['r', 'r', 'r']
            ],
            [
                ["b", "b", "b"],
                ["b", "b", "b"],
                ["b", "b", "b"]
            ],
            [
                ["o", "o", "o"],
                ["o", "o", "o"],
                ["o", "o", "o"]
            ],
            [
                ["g", "g", "g"],
                ["g", "g", "g"],
                ["g", "g", "g"]
            ],
            [
                ["y", "y", "y"],
                ["y", "y", "y"],
                ["y", "y", "y"]
            ]
        ]
        self.rotation_map = {
            "U" : [1,2,3,4] ,
            "U'" : [4,3,2,1],
            "D" : [4,3,2,1],
            "D'" : [1,2,3,4],
            "L" : [1,0,3,5],
            "L'" : [5,3,0,1],
            "R" : [0,1,5,3],
            "R'" : [3,5,1,0],
            "F" : [0,4,5,2],
            "F'" : [2,5,4,0],
            "B" : [0,2,5,4],
            "B'" : [4,5,2,0]
        }

    def scramble(self):
        for i in range(100):
            self.rotate(random.choice(list(self.rotation_map.keys())))

    def rotate(self, notation):
        impact_faces = self.rotation_map[notation]
        if notation == "U" or notation == "U'":
            self.up_movement(impact_faces)
        elif notation == "D" or notation == "D'":
            self.down_movement(impact_faces)
        elif notation == "L" or notation == "L'":
            self.left_movement(impact_faces)
        elif notation == "R" or notation == "R'":
            self.right_movement(impact_faces)
        elif notation == "F" or notation == "F'":
            self.front_movement(notation, impact_faces)
        elif notation == "B" or notation == "B'":
            self.back_movement(notation, impact_faces)

    def up_movement(self, impact_faces):
        memory = self.cube[impact_faces[0]][0]
        for face in impact_faces:
            if face == impact_faces[3]:
                self.cube[face][0] = memory
                return self.cube
            next_face = impact_faces[impact_faces.index(face) + 1]
            self.cube[face][0] = self.cube[next_face][0]
            
    def down_movement(self, impact_faces):
        memory = self.cube[impact_faces[0]][2]
        for face in impact_faces:
            if face == impact_faces[3]:
                self.cube[face][2] = memory
                return self.cube
            next_face = impact_faces[impact_faces.index(face) + 1]
            self.cube[face][2] = self.cube[next_face][2]
            
    def left_movement(self, impact_faces):
        memory = [self.cube[impact_faces[0]][0][0], self.cube[impact_faces[0]][1][0], self.cube[impact_faces[0]][2][0]]
        for face in impact_faces:
            if face == impact_faces[3]:
                self.cube[face][0][0] = memory[0]
                self.cube[face][1][0] = memory[1]
                self.cube[face][2][0] = memory[2]
                return self.cube
            next_face = impact_faces[impact_faces.index(face) + 1]
            self.cube[face][0][0] = self.cube[next_face][0][0]
            self.cube[face][1][0] = self.cube[next_face][1][0]
            self.cube[face][2][0] = self.cube[next_face][2][0]

    def right_movement(self, impact_faces):
        memory = [self.cube[impact_faces[0]][0][2], self.cube[impact_faces[0]][1][2], self.cube[impact_faces[0]][2][2]]
        for face in impact_faces:
            if face == impact_faces[3]:
                self.cube[face][0][2] = memory[0]
                self.cube[face][1][2] = memory[1]
                self.cube[face][2][2] = memory[2]
                return self.cube
            next_face = impact_faces[impact_faces.index(face) + 1]
            self.cube[face][0][2] = self.cube[next_face][0][2]
            self.cube[face][1][2] = self.cube[next_face][1][2]
            self.cube[face][2][2] = self.cube[next_face][2][2]

    def front_movement(self, notation, impact_faces):
        if notation == "F":
            memory = [self.cube[0][2][0], self.cube[0][2][1], self.cube[0][2][2]]  # White row 2
            self.cube[0][2][0], self.cube[0][2][1], self.cube[0][2][2] = self.cube[4][0][2], self.cube[4][1][2], self.cube[4][2][2]  # White ← Green col 2
            self.cube[4][0][2], self.cube[4][1][2], self.cube[4][2][2] = self.cube[5][0][0], self.cube[5][0][1], self.cube[5][0][2]  # Green ← Yellow row 0
            self.cube[5][0][0], self.cube[5][0][1], self.cube[5][0][2] = self.cube[2][2][0], self.cube[2][1][0], self.cube[2][0][0]  # Yellow ← Blue col 0 (reversed)
            self.cube[2][0][0], self.cube[2][1][0], self.cube[2][2][0] = memory[0], memory[1], memory[2]  # Blue ← saved White row 2
        else: #Reverse notation
            memory = [self.cube[2][0][0], self.cube[2][1][0], self.cube[2][2][0]]  # Blue col 0
            self.cube[2][0][0], self.cube[2][1][0], self.cube[2][2][0] = self.cube[5][0][2], self.cube[5][0][1], self.cube[5][0][0]  # Blue ← Yellow row 0 (reversed)
            self.cube[5][0][0], self.cube[5][0][1], self.cube[5][0][2] = self.cube[4][0][2], self.cube[4][1][2], self.cube[4][2][2]  # Yellow ← Green col 2
            self.cube[4][0][2], self.cube[4][1][2], self.cube[4][2][2] = self.cube[0][2][0], self.cube[0][2][1], self.cube[0][2][2]  # Green ← White row 2
            self.cube[0][2][0], self.cube[0][2][1], self.cube[0][2][2] = memory[0], memory[1], memory[2]  # White ← saved Blue col 0
        return self.cube

    def back_movement(self, notation, impact_faces):
        if notation == "B":
            memory = [self.cube[0][0][0], self.cube[0][0][1], self.cube[0][0][2]]  # White row 0
            self.cube[0][0][0], self.cube[0][0][1], self.cube[0][0][2] = self.cube[4][0][0], self.cube[4][1][0], self.cube[4][2][0]  # White ← Green col 0
            self.cube[4][0][0], self.cube[4][1][0], self.cube[4][2][0] = self.cube[5][2][2], self.cube[5][2][1], self.cube[5][2][0]  # Green ← Yellow row 2 (reversed)
            self.cube[5][2][0], self.cube[5][2][1], self.cube[5][2][2] = self.cube[2][2][2], self.cube[2][1][2], self.cube[2][0][2]  # Yellow ← Blue col 2 (reversed)
            self.cube[2][0][2], self.cube[2][1][2], self.cube[2][2][2] = memory[0], memory[1], memory[2]  # Blue ← saved White row 0
        else: #Reverse notation
            memory = [self.cube[4][0][0], self.cube[4][1][0], self.cube[4][2][0]]  # Green col 0
            self.cube[4][0][0], self.cube[4][1][0], self.cube[4][2][0] = self.cube[2][2][2], self.cube[2][1][2], self.cube[2][0][2]  # Green ← Blue col 2 (reversed)
            self.cube[2][0][2], self.cube[2][1][2], self.cube[2][2][2] = self.cube[5][2][2], self.cube[5][2][1], self.cube[5][2][0]  # Blue ← Yellow row 2 (reversed)
            self.cube[5][2][0], self.cube[5][2][1], self.cube[5][2][2] = self.cube[0][0][0], self.cube[0][0][1], self.cube[0][0][2]  # Yellow ← White row 0
            self.cube[0][0][0], self.cube[0][0][1], self.cube[0][0][2] = memory[0], memory[1], memory[2]  # White ← saved Green col 0
        return self.cube
