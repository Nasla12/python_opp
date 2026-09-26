class studentclass:
    def __init__(self):
        self.date_of_birth = None
        self.age = None
        self.gender = None
        self.mobile_number = None
        self.email_address = None
        self.preferred_language = None
        self.school_college_name = None
        self.class_grade = None
        self.board_curriculum = None
        self.academic_year = None
        self.subjects_for_tuition = []
        self.current_level_by_subject = {}
        self.areas_need_help = []

        self.parent_guardian_name = None
        self.relationship_with_student = None
        self.parent_mobile_number = None
        self.parent_email_address = None
        self.preferred_communication_method = None

        self.parent_guardian_details = {
            "name": self.parent_guardian_name,
            "relationship_with_student": self.relationship_with_student,
            "mobile_number": self.parent_mobile_number,
            "email_address": self.parent_email_address,
            "preferred_communication_method": self.preferred_communication_method,
        }

    
        )
