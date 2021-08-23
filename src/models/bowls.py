"""
Model for a bowling run

Currently fairly empty as no DB connected but could be reworked
Mostly contains functions for a bowling run
"""
# ==============================================================================
# ==============================================================================


class Bowl:
    def __repr__(self):
        pass

    @classmethod
    def get_score(cls, input_scores):
        """Gets a full bowl for a person

        This includes all bowls for an entire game for 1 person
        """

        final_score = 0

        frame_balls = 0
        frame_score = 0
        frame_number = 1

        for i, score in enumerate(input_scores):
            final_score += score
            frame_score += score
            frame_balls += 1

            if frame_number < 10:
                if frame_score == 10:  # end frame
                    if frame_balls == 1:  # strike
                        final_score += input_scores[i + 1] + input_scores[i + 2]

                    else:  # spare
                        final_score += input_scores[i + 1]

                    frame_score = 0
                    frame_balls = 0
                    frame_number += 1

                elif frame_balls == 2:  # enough balls for frame
                    frame_number += 1
                    frame_balls = 0
                    frame_score = 0

        return final_score
