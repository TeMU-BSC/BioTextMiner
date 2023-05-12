-- SCRIPT : BD SQL
-- DATE   : 26/01/2023
-- AUTHOR : SIDDIQUE MUHAMMAD


-- CREATE DATABASE
DROP DATABASE fct;
CREATE DATABASE fct;
use fct;


-- CREATE TABLES
-- TABLE : users
-- Description : Stores the users information. 
-- Necessary for login and register.
CREATE TABLE users (
    user_id INTEGER NOT NULL AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL unique,
    password VARCHAR(50) NOT NULL,
    name VARCHAR(50) NOT NULL,
    surname VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    role VARCHAR(50) NOT NULL,
    PRIMARY KEY (user_id)
);

-- CREATE TABLES
-- TABLE : documents
CREATE TABLE documents(
    text_id INTEGER AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    date VARCHAR(50),
    author VARCHAR(50),
    source VARCHAR(50),
    collection VARCHAR(50),
    language VARCHAR(10),
    PRIMARY KEY (text_id)
);


-- TABLE : corpus
CREATE TABLE corpus (
    corpus_id INTEGER AUTO_INCREMENT,
    corpus_name VARCHAR(50) NOT NULL,
    labels VARCHAR(100),
    description VARCHAR(3000),
    version VARCHAR(15),
    n_docs VARCHAR(10),
    PRIMARY KEY(corpus_id)
);


-- TABLE : specialties
CREATE TABLE specialties (
    specialty_id INTEGER AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    description VARCHAR(500),
    PRIMARY KEY (specialty_id)
);


-- TABLE : document_corpus
-- text_id references the text_id in documents table.
-- corpus_id references the corpus_id in corpus table.
-- the structure have to be same in both tables. 
-- the columns have be Primary key in documents and corpus tables.
CREATE TABLE document_corpus (
    text_id INTEGER REFERENCES documents(text_id) ,
    corpus_id INTEGER REFERENCES corpus(corpus_id) ,
    PRIMARY KEY (text_id, corpus_id)
);


-- TABLE : document_specialties
-- text_id references the text_id in documents table.
-- specialty_id references specialty id in specialties tables
-- the structure have to be same in both tables. 
-- the columns have be Primary key in documents and specialties tables.
CREATE TABLE document_specialties (
    text_id INTEGER REFERENCES documents(text_id),
    specialty_id INTEGER REFERENCES specialties(specialty_id),
    PRIMARY KEY (text_id, specialty_id)
);


-- TABLE : annotations
-- corpus_id references corpus_id in corpus table
-- text_id references text_id in documents tables
CREATE TABLE annotations (
    ann_id INTEGER AUTO_INCREMENT,
    corpus_id INTEGER,
    text_id INTEGER NOT NULL, 
    ann_text VARCHAR(500),
    start_span INTEGER, 
    end_span INTEGER, 
    norm_id VARCHAR(25), 
    attributes VARCHAR(500),
    mark VARCHAR(20),
    PRIMARY KEY (ann_id)
);


-- TABLE : ontologies
CREATE TABLE ontologies(
    ontology_id INTEGER AUTO_INCREMENT,
    name VARCHAR(100),
    version VARCHAR(15),
    language VARCHAR(10),
    description VARCHAR(500),
    PRIMARY KEY (ontology_id)
);


-- TABLE : normalizations
-- ontology_id references ontology_id in ontologies tables
-- code_id references code_id in ontology_ontology_descriptors tables. Created manually
CREATE TABLE normalizations (
    norm_id VARCHAR(25) NOT NULL,
    ontology_id INTEGER,
    code_id INTEGER, 
    semantic_relation VARCHAR(50),
    PRIMARY KEY(norm_id)
);


-- TABLE : ontology_descriptors
-- code_id : created by the programmer. Primary key of this table
-- descriptor_id : id in the csv file
-- ontology_id references ontology_id in ontologies tables
CREATE TABLE ontology_descriptors (
    code_id INTEGER AUTO_INCREMENT,
    descriptor_id VARCHAR(200) NOT NULL,
    ontology_id INTEGER, 
    descriptor VARCHAR(500),
    semantic_label VARCHAR(100),
    language VARCHAR(10),
    term_type VARCHAR(100),
    PRIMARY KEY (code_id)
);


-- TABLE : ontology_ontology_descriptors
-- Description: Relation table between ontology and ontology_descriptors
-- code_id references the primmary key in the table ontology_descriptors . Created by the programme.
-- ontology_id references ontology_id in ontologies table
CREATE TABLE ontology_ontology_descriptors(
    ontology_id INTEGER,
    code_id INTEGER,
    PRIMARY KEY(ontology_id, code_id)
);


-- ALTER TABLES
-- ADD FOREIGN KEYS
-- Table : annotations
ALTER TABLE annotations ADD FOREIGN KEY (text_id) REFERENCES documents(text_id);


-- Table : normalizations
ALTER TABLE normalizations ADD FOREIGN KEY (ontology_id) REFERENCES ontologies(ontology_id);
ALTER TABLE normalizations ADD FOREIGN KEY (code_id) REFERENCES ontology_descriptors(code_id);


-- Table : ontology_descriptors
ALTER TABLE ontology_descriptors ADD FOREIGN KEY (ontology_id) REFERENCES ontologies (ontology_id);


-- Table : ontology_ontology_descriptors
ALTER TABLE ontology_ontology_descriptors ADD FOREIGN KEY (ontology_id) REFERENCES ontologies (ontology_id);
ALTER TABLE ontology_ontology_descriptors ADD FOREIGN KEY (code_id) REFERENCES ontology_descriptors (code_id);


-- Insert values for testing
-- Table : documents
insert into documents values(1, 'file1.txt', '2023-02-15', 'siddique','ncbi', 'collection1', 'es');
insert into documents values(2, 'file2.txt', '2023-02-16', 'siddique','biomedical', 'collection2', 'en');
insert into documents values(3, 'file3.ann', '2023-02-16', 'siddique','biomedical', 'collection3', 'es');
insert into documents values(4, 'file4.txt', '2023-02-16', 'siddique','ncbi', 'collection4', 'es');
insert into documents values(5, 'file5.ann', '2023-02-18', 'siddique','ncbi', 'collection5', 'es');
insert into documents values(6, 'file6.txt', '2023-02-18', 'siddique','ncbi', 'collection6', 'es');
insert into documents values(7, 'file7.ann', '2023-03-10', 'siddique','ncbi', 'collection7', 'en');

-- Table : corpus
insert into corpus values(1, 'distemist', 'corpus', 'this is a corpus', '1.0', '100');
insert into corpus values(2, 'distemist', 'corpus', 'this is a corpus', '1.0', '100');	
insert into corpus values(3, 'biomed', 'corpus', 'this is a corpus', '2.0', '340');
insert into corpus values(4, 'biomed', 'corpus', 'this is a corpus', '2.0', '124');
insert into corpus values(5, 'biomed', 'corpus', 'this is a corpus', '2.0', '124');
insert into corpus values(6, 'biomed', 'corpus', 'this is a corpus', '5.0', '432');
insert into corpus values(7, 'corpusdis', 'corpus', 'this is a corpus', '5.3', '232');

-- Table : document_corpus
insert into document_corpus values(1, 1);
insert into document_corpus values(1, 2);
insert into document_corpus values(3, 5);
insert into document_corpus values(6, 5);

-- Table : specialties
insert into specialties values (1, 'covid', 'this is a covid specialty');
insert into specialties values (2, 'medicina_interna', 'about medicine');
insert into specialties values (3, 'neurologia', 'about neurology');
insert into specialties values (4, 'odontologia', 'topic odontology');
insert into specialties values (5, 'atencion_primaria', 'primary atention specialty');

-- Table : document_specialties
insert into document_specialties values(1, 2);
insert into document_specialties values(1, 4);
insert into document_specialties values(5, 4);
insert into document_specialties values(4, 3);
insert into document_specialties values(7, 3);

-- Table : annotations
insert into annotations values(1, 1, 1, 'annotation in text', 2,5,1,'attr1', 'abjjr');
insert into annotations values(2, 7, 2, 'annotation in text', 2,5,1,'attr1', 'abjjr');
insert into annotations values(3, 5, 4, 'annotation in text', 2,3,3,'attr1', 'abjjr');
insert into annotations values(4, 6, 3, 'annotation in text', 2,3,4,'attr2', 'abjjr');
INSERT INTO annotations(ann_id, corpus_id, text_id, ann_text, start_span, end_span, norm_id, attributes, mark) VALUES (5, 1,1,'annke3',1,3,1,'attrr1','nkevee');

-- Table : ontologies
insert into ontologies values(1, 'name1','1.0','es','desc01');
insert into ontologies values(2, 'name2','1.0','es','desc02');
insert into ontologies values(3, 'name3','1.2','es','desc04');
insert into ontologies values(4, 'name3','1.2','es','desc03');
insert into ontologies values(5, 'name5','1.5','es','desc05');	
-- Table : ontology_descriptors
insert into ontology_descriptors values(1, 1, 1, 'desc01', 'label01','es','type01');
insert into ontology_descriptors values(2, 2, 2, 'desc02', 'label02','es','type02');
insert into ontology_descriptors values(3, 3, 3, 'desc03', 'label03','en','type03');
insert into ontology_descriptors values(4, 4, 4, 'desc04', 'label04','es','type04');
insert into ontology_descriptors values(5, 5, 5, 'desc05', 'label05','en','type05');


-- Table : normalizations
insert into normalizations values(1, 1, 1, 'rel1');
insert into normalizations values(2, 2, 2, 'rel2');
insert into normalizations values(3, 3, 3, 'rel3');

-- Table : ontology_ontology_descriptors
insert into ontology_ontology_descriptors values(1, 1);
insert into ontology_ontology_descriptors values(1, 3);
insert into ontology_ontology_descriptors values(2, 5);
insert into ontology_ontology_descriptors values(3, 4);
insert into ontology_ontology_descriptors values(4, 4);
insert into ontology_ontology_descriptors values(2, 3);

-- Table : users
INSERT INTO users(username, password, name, surname, email, role) VALUES('user01', 'pass01', 'Juan', 'Antonio', 'user1@gmail.com', 'guest');
INSERT INTO users(username, password, name, surname, email, role) VALUES('user02', 'pass02', 'Joana', 'Perez', 'user2@gmail.com', 'annotator');
INSERT INTO users(username, password, name, surname, email, role) VALUES('user03', 'pass03', 'Jose', 'Martinez', 'user3@gmail.com', 'admin');
INSERT INTO users(username, password, name, surname, email, role) VALUES('user04', 'pass04', 'Mireia', 'Perez', 'user4@gmail.com', 'guest');
INSERT INTO users(username, password, name, surname, email, role) VALUES('user05', 'pass05', 'Bob', 'Martinez', 'user5@gmail.com', 'annotator');
