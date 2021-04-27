from validate_docbr import CPF
import string


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


class InputVeirfy:
    def verifyinputs(self, fullname, birth, cpf, height) -> bool:
        if not self.validate_name(fullname):
            print(f"{bcolors.WARNING}O nome inserido é inválido!{bcolors.ENDC}")
            return False
        if not self.validate_cpf(cpf):
            print(f"{bcolors.WARNING}O CPF inserido é inválido!{bcolors.ENDC}")
            return False
        if not self.validade_date(birth):
            print(f"{bcolors.WARNING}A data de nascimento inserida é inválida!{bcolors.ENDC}")
            return False
        if not self.validate_height(height):
            print(f"{bcolors.WARNING}A altura inserida é inválida!{bcolors.ENDC}")
            return False
        return True

    def validate_name(self, fullname) -> bool:
        for i in fullname:
            if not i.lower() in string.ascii_letters and not i == " ":
                return False
        return True

    def validate_cpf(self, cpf) -> bool:
        if CPF().validate(cpf):
            return True
        else:
            return False

    def validade_date(self, date) -> bool:
        date = date.split("/")
        if not len(date) == 3:
            return False
        if not len(date[0]) == 2:
            return False
        if not len(date[1]) == 2:
            return False
        if not len(date[2]) == 4:
            return False
        return True

    def validate_height(self, height) -> bool:
        if type(height) == float:
            return True
        else:
            return False
