from banco import Banco
from tkinter import messagebox

class Cidades(object):

    def __init__(self,idcidade = 0, nomecid= "", uf = ""):
        self.info={}
        self.idcidade = idcidade
        self.nomecid = nomecid
        self.uf      = uf

    def insertcid(self):
        banco = Banco()
        try:
            c= banco.conexao.cursor()
            c.execute("insert into tbl_cidades(nomecid,uf) values('" + self.nomecid + "', '" + self.uf + "')")
            banco.conexao.commit()
            c.close()
            messagebox.showinfo('Sucesso','Cidade cadastrada com sucesso!')
        except:
            messagebox.showinfo('Erro','Ocorreu um erro no cadastro!')

    def updatecid(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("update tbl_cidades set nomecid = '" + self.nomecid + "', uf = '" + self.uf + "'  where idcidade = " + self.idcidade + " ")
            banco.conexao.commit()
            c.close()
            messagebox.showinfo('Sucesso','Cidade alterada com sucesso!')
        except:
            messagebox.showinfo('Erro','Ocorreu um erro na alteração na alteração da cidade!')

    def excluircid(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("delete from tbl_cidades where idcidade = " + self.idcidade + " ")
            banco.conexao.commit()
            c.close()
            messagebox.showinfo("Sucesso",'Registro apagado com sucesso!')
        except:
            messagebox.showinfo("Erro",'Ocorreu um erro na exclusão!')

    def selectcid(self,idcidade):
        banco = Banco()
        try :
            c = banco.conexao.cursor()
            c.execute("select  * from tbl_cidades where idcidade = "+ idcidade +"  ")
            for linha in c:
                self.idcidade = linha[0]
                self.nomecid = linha[1]
                self.uf = linha[2]

                c.close()
                messagebox.showinfo("Sucesso","Busca feita com sucesso!")

        except:
                messagebox.showinfo("Erro","Ocorreu um erro na busca do usuário")
