CREATE TABLE Korisnik (
    email VARCHAR(25) PRIMARY KEY,
    lozinka VARCHAR(18)
);

CREATE TABLE Pitanje (
    id_pitanja VARCHAR(255) PRIMARY KEY,
    tekst_pitanja char(200)
);

CREATE TABLE Odgovor (
    id_odgovora VARCHAR2(255) PRIMARY KEY ,
    tekst_ODGOVORA CHAR(255),
    id_pitanja VARCHAR(255),
    email_korisnika VARCHAR(25),
    FOREIGN KEY (id_pitanja) REFERENCES Pitanje(id_pitanja),
    FOREIGN KEY (email_korisnika) REFERENCES Korisnik(email)
);