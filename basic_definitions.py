# -*- coding: utf-8 -*-

class constants(object):
    def __init__(self):

        # ACHTUNG: Diese Variablennamen dürfen nicht geändert werden, da sie aus dem Programm aufgerufen und ausgelesen
        #           werden. Genauer: im Einstellungsmenu lässt sich die Verbindung zur Datenbank einstellen. Falls sie
        #           sich ändert, wird dieser Datei hier, umgeschrieben. Die Variablennamen sind dabei die Keywörter für
        #           die Methode save in Ui_Settings.py. Ebenso wird beim Öffnen der Einstellungen aus dieser Datei
        #           die aktuellen Werte anhand der Variablennamen gelesen.
        self.DB_host = 'localhost'
        self.DB_user = 'root'
        self.DB_port = 3306
        self.DB_database = 'beringung'
        self.ringnummern_laenge = 8
        self.key = b'7mwDo5p3mft4qW3DJzhwKzC65vgYWgW45FhL_0DOg2E='
        # Heidi's database
        self.DB_password = b'gAAAAABmOMCnP_LRczh4eS3XUkz91m7h67mJI09tLazUcKE9k8acbosM5I6_ALrWvsg-o-8I2lCb2jquJGvE-Y8FVg5xrn9HqQ=='
        #
        #           Die obige Bemerkung gilt bis hier!
        #
        #
        self.hilfeBilderPfad = 'C:/Users/wicht/PycharmProjects/DB_connection/Bilder/Hilfe/'
        self.debug = True
        self.mit_anmeldung = True
        self.tbl_name_ringserie = 'ringserie_neu'
        self.age_adult_allowed = False
        self.zoom_seitenbreite = True
        self.version = '0.1'
        self.kontaktdaten = f'Stefan Bongers, mail@sseyfert.de, +49 176 2465 1751\nThomas Jascke, ??@??.??, +49 ... .... ....'

    def get_key(self):
        return self.key

    def get_p(self):
        return self.DB_password

    def get_ringnummern_laenge(self):
        return self.ringnummern_laenge

    def set_debug(self, status: bool = False):
        self.debug = status

    def get_debug(self) -> bool:
        """

        :return:
        TRUE : wenn Debug-Status AN/ON/TRUE
        FALSE : wenn Debug-Status AUS/OFF/FALSE
        """
        return self.debug

    def get_mit_anmeldung(self):
        return self.mit_anmeldung

    def get_host(self):
        return self.DB_host

    def get_port(self):
        return self.DB_port

    def get_database(self):
        return self.DB_database

    def get_user(self):
        return self.DB_user

    def get_hilfepfad(self):
        return self.hilfeBilderPfad

    def get_tbl_name_ringserie(self):
        return self.tbl_name_ringserie

    def get_age_adult_allowed(self):
        return self.age_adult_allowed

    def get_zoom_seitenbreite(self):
        return self.zoom_seitenbreite

    def get_version(self):
        return self.version

    def get_kontaktdaten(self):
        return self.kontaktdaten
