import MySQLdb
import InputVerifier
iv = InputVerifier.InputVeirfy()


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Database:
    conn = MySQLdb.connect(db="proway", host="localhost", user="root")
    cursor = conn.cursor()


class Users(Database):
    def insert_user(self, fullname, birth, cpf, height) -> bool:
        if not iv.verifyinputs(fullname, birth, cpf, height): return False
        print(iv.verifyinputs(fullname, birth, cpf, height))
        try:
            self.cursor.execute(f"INSERT INTO users (fullname, birth, cpf, height) VALUES "
                                f"('{fullname}', '{birth}', '{cpf}', '{height}')")
            self.conn.commit()
            print(f"{bcolors.OKGREEN}Usuário adiconado com sucesso ao banco de dados!{bcolors.ENDC}")
        except:
            print("Não foi possivel inserir o usuário no banco de dados!")
            return False
        return True

    def update_user(self, id, fullname, birth, cpf, height) -> bool:
        iv.verifyinputs(fullname, birth, cpf, height)
        try:
            self.cursor.execute(f"UPDATE users SET fullname='{fullname}', birth='{birth}', cpf='{cpf}', height='{height}' "
                                f"WHERE id='{id}'")
            self.conn.commit()
        except:
            print(f"{bcolors.FAIL}Não foi possível atualizar o usuário!{bcolors.ENDC}")
            return False
        return True

    def update_all(self, fullname, birth, cpf, height):
        iv.verifyinputs(fullname, birth, cpf, height)
        try:
            self.cursor.execute(f"UPDATE users SET fullname='{fullname}', birth='{birth}', cpf='{cpf}', height='{height}'")
            self.conn.commit()
        except:
            print(f"{bcolors.FAIL}Não foi possível atualizar todos os usuários!{bcolors.ENDC}")
            return False
        return True

    def get_users(self) -> (bool, tuple):
        try:
            self.cursor.execute("SELECT * FROM users")
            return self.cursor.fetchall()
        except:
            print(f"{bcolors.FAIL}Não foi possível localizar os usuários!{bcolors.ENDC}")
            return False

    def list_users(self):
        try:
            self.cursor.execute("SELECT * FROM users")
            result = self.cursor.fetchall()
        except:
            print("Não foi possível localizar os usuários!")
            return False
        print("NOME COMPLETO - DATA DE NASCIMENTO - CPF - ALTURA")
        for i in result:
            print(f"{i[1]} - {i[2]} - {i[3]} - {i[4]}")
        return True


    def get_user(self, field, value):
        try:
            self.cursor.execute(f"SELECT * FROM users WHERE {field}={value}")
            return self.cursor.fetchall()
        except:
            print(f"{bcolors.FAIL}Não foi possível localizar o usuário!{bcolors.ENDC}")
            return False

    def delete_user(self, id):
        try:
            self.cursor.execute(f"DELETE FROM users WHERE id={id}")
            self.conn.commit()
        except:
            print(f"{bcolors.FAIL}Não foi possível apagar o usuário!{bcolors.ENDC}")
            return False
        return True

    def delete_all(self):
        try:
            self.cursor.execute(f"DELETE FROM users")
            self.conn.commit()
        except:
            print(f"{bcolors.FAIL}Não foi possível apagar todos os usuários!{bcolors.ENDC}")
            return False
        return True
