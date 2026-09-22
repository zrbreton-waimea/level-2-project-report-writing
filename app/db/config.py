#============================================================================
# Database schema and seed data configuration
#============================================================================


#----------------------------------------------------------------------------
# Table definitions
#----------------------------------------------------------------------------
# Define your tables with a name, a schema and optional seed/sample data,
# using this format, and then add the tables to the Table Registry below:
#
# class TableName:
#     NAME      = "name"
#     SCHEMA    = "CREATE TABLE name (...)"
#     SEED_DATA = "INSERT INTO name (...)" or None
#----------------------------------------------------------------------------

class reports:

    NAME = "reports"

    SCHEMA = """
        CREATE TABLE reports(
            id      INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id   TEXT NOT NULL,
            term    INTEGER,
            maths   INTEGER,
            writing INTEGER,
            reading INTEGER,
            overall_comment  TEXT NOT NULL
        )
    """

    SEED_DATA = """
        INSERT INTO reports (student_id, term, overall_comment)
        VALUES
            ("AD2231", 1, "[Student Name] consistently displays a positive attitude toward learning and school life, acting as a conscientious and enthusiastic learner who takes pride in their work. They work well independently and are always willing to help peers, showing wonderful enthusiasm and bringing great energy to classroom discussions."),
            ("AD8392", 1, "[Student Name] reads with good fluency and is developing a strong vocabulary, with writing pieces becoming increasingly detailed and imaginative. They listen attentively during shared reading and contribute thoughtful ideas, though they occasionally need to focus on checking spelling and punctuation during independent writing tasks."),
            ("AD1312",   1, "Demonstrating a solid grasp of fundamental mathematical concepts, [Student Name] works accurately with addition and subtraction strategies. They enjoy solving hands-on math problems and working with peers, while continuing to benefit from extra practice with multiplication tables to boost speed.")
    """

class students:

    NAME = "students"

    SCHEMA = """
        CREATE TABLE students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        
        FOREIGN KEY(id) REFERENCES reports(id)
        )
    """

    SEED_DATA = """
        INSERT INTO students (name)
        VALUES
            ("Celia Arellano"   ),
            ("Brylee Knapp"     ),
            ("Tru Kim"          ),
            ("Branson Mitchell" )
    """

class maths:

    NAME = "maths"

    SCHEMA = """
        CREATE TABLE maths (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        measurement  INTEGER,
        algebra      INTEGER,
        number       INTEGER,
        geometry     INTEGER,
        statistics   INTEGER,
        comment TEXT NOT NULL,

        
        FOREIGN KEY(id) REFERENCES reports(id)
        )
    """

    SEED_DATA = """
        INSERT INTO maths (measurement, algebra, number, geometry, statistics, comment)
        VALUES
            ( 4, 2, 4, 4, 5, "[Student Name] demonstrates an exceptional understanding of mathematical concepts and consistently applies creative problem-solving strategies to complex tasks. They show strong fluency with number facts and explain their mathematical reasoning clearly both verbally and in writing. Next step: Tackle open-ended extension challenges, particularly multi-step word problems requiring spatial reasoning." ),
            ( 2, 2, 2, 3, 3, "[Student Name] has made steady progress in mathematics this term and confidently handles core grade-level concepts, including place value and basic operations. They work well during independent practice and complete daily problem-solving tasks with good accuracy. Next step: Focus on strengthening instant recall of multiplication facts to increase calculation speed." ),
            ( 4, 4, 4, 4, 4, "[Student Name] demonstrates an exceptional understanding of mathematical concepts and consistently applies creative problem-solving strategies to complex tasks. They show strong fluency with number facts and explain their mathematical reasoning clearly both verbally and in writing. Next step: Tackle open-ended extension challenges, particularly multi-step word problems requiring spatial reasoning." ),
            ( 3, 4, 4, 2, 3, "[Student Name] shows enthusiasm during practical math activities and is gaining confidence when working with numbers up to 100. They benefit from using visual models and concrete materials to support their understanding of multi-step concepts. Next step: Continue practicing basic addition and subtraction strategies and build confidence in interpreting mathematical word problems." )
    """

class reading:

    NAME = "reading"

    SCHEMA = """
        CREATE TABLE reading (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        recognition       INTEGER,
        comprehension     INTEGER,
        critical_analysis INTEGER,
        comment           TEXT NOT NULL,

        
        FOREIGN KEY(id) REFERENCES reports(id)
        )
    """

    SEED_DATA = """
        INSERT INTO reading (recognition, comprehension, critical_analysis, comment)
        VALUES
            ( 4, 2, 4, "[Student Name] is an exceptional reader who comprehends complex texts well above grade level. They consistently analyze character motivations, identify theme and main ideas, and make thoughtful inferences supported by evidence from the text. Next step: Explore non-fiction genres and technical vocabulary to broaden critical reading skills across different subject areas." ),
            ( 2, 2, 2, "[Student Name] is a confident reader who accurately decodes familiar texts and reads aloud with good fluency and expression. They answer literal comprehension questions easily and are beginning to infer deeper meanings during class discussions. Next step: Focus on summarizing longer chapters concisely, identifying key details without retelling every event." ),
            ( 4, 4, 4, "[Student Name] is an exceptional reader who comprehends complex texts well above grade level. They consistently analyze character motivations, identify theme and main ideas, and make thoughtful inferences supported by evidence from the text. Next step: Explore non-fiction genres and technical vocabulary to broaden critical reading skills across different subject areas." ),
            ( 3, 4, 3, "[Student Name] is making steady progress with decoding strategies and shows enthusiasm during guided reading sessions. They respond well to visual prompts and context clues to figure out unfamiliar words. Next step: Practice daily sight-word recall and blend phonics sounds to build reading fluency and confidence." )
    """

class writing:

    NAME = "writing"

    SCHEMA = """
        CREATE TABLE writing (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        transcription     INTEGER,
        composition       INTEGER,
        writing_process   INTEGER,
        comment           TEXT NOT NULL,

        
        FOREIGN KEY(id) REFERENCES reports(id)
        )
    """

    SEED_DATA = """
        INSERT INTO writing (transcription, composition, writing_process, geometry, comment)
        VALUES
            ( 4, 2, 4, "[Student Name] is a creative and articulate writer who consistently produces highly detailed and well-structured pieces across various genres. They demonstrate an advanced command of vocabulary, sentence structure, and punctuation to engage the reader effectively. Next step: Focus on revising and editing drafts to refine figurative language and elevate tone for specific target audiences." ),
            ( 2, 2, 2, "[Student Name] enjoys sharing ideas verbally and is making steady progress translating those thoughts into written form. They are building confidence in basic sentence structure, using capital letters, and ending sentences with full stops. Next step: Practice using phonics knowledge and personal word banks to independently spell unfamiliar words." ),
            ( 4, 4, 4, "[Student Name] is a creative and articulate writer who consistently produces highly detailed and well-structured pieces across various genres. They demonstrate an advanced command of vocabulary, sentence structure, and punctuation to engage the reader effectively. Next step: Focus on revising and editing drafts to refine figurative language and elevate tone for specific target audiences." ),
            ( 3, 4, 4, "[Student Name] writes clearly and confidently, organizing ideas into structured paragraphs with distinct beginnings, middles, and endings. They reliably apply taught grammar rules, punctuation, and spelling strategies to their daily work. Next step: Incorporate more varied sentence openers and descriptive vocabulary to enrich narrative writing." )
    """

# Add more table classes here...



#----------------------------------------------------------------------------
# Table registry
#----------------------------------------------------------------------------
# Register all of your tables by adding them to the TABLES list here:
#
# TABLES = [
#     Table1Name,
#     Table2Name,
#     etc.
# ]
#
# Note: The table order is important - Create the tables that have
# foreign keys *after* the tables they link to have been created
#----------------------------------------------------------------------------

TABLES = [
    students, reports, maths, reading, writing
    # Add more tables here...
]

