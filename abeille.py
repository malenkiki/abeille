#!/usr/bin/python
# -*- coding: utf-8 -*-

import  wx

class Abeille(wx.App):
    def OnInit(self):
        self.frame = MainFrame(None, title="Abeille")
        self.SetTopWindow(self.frame)
        self.frame.Show()

        return True

class MainFrame(wx.Frame):
    def __init__(self, parent, id=wx.ID_ANY, title="", 
                 pos=wx.DefaultPosition, size=wx.DefaultSize,
                 style=wx.DEFAULT_FRAME_STYLE,
                 name="MainFrame"):
        super(MainFrame, self).__init__(parent, id, title,
                                      pos, size, style, name)

        self.panel = wx.Panel(self)
        self.menu()


    def menu(self):
        menuBar = wx.MenuBar()

        menu1 = wx.Menu()
        menu1.Append(101, "&Comptes…", "Entrez ou modifiez vos identifiants, vos serveurs…")
        menu1.Append(102, "&Paramètres…", "Paramètrez Abeille")
        menu1.AppendSeparator()
        menu1.Append(103, "&Quitter", "Quitter l’application")
        menuBar.Append(menu1, "Application")

        menu2 = wx.Menu()
        menu2.Append(201, "Nouveau…", "Créer un nouveau projet.")
        menu2.Append(202, "Ouvrir…", "Ouvre un projet existant.")
        menu2.Append(203, "Fermer", "Ferme le projet courant")
        menu2.AppendSeparator()
        menu2.Append(204, "Configurer…", "Paramètrer le projet courant.")
        menu2.AppendSeparator()
        menu2.Append(205, "Tous les projets…", "Affiche tous les projets dans une liste pour choisir le bon.")
        menu2.AppendSeparator()
        # Les trois items suivants seront dynamiques
        menu2.Append(206, "Un Projet", "")
        menu2.Append(207, "Un Autre Projet", "")
        menu2.Append(208, "Encore un autre projet", "")
        menuBar.Append(menu2, "&Projets")

        menu3 = wx.Menu()

        subMenu301 = wx.Menu()
        subMenu302 = wx.Menu()
        subMenu303 = wx.Menu()

        subMenu301.Append(3011, "Créer", "Ouvre un nouveau ticket pour le projet en cours.")
        subMenu301.Append(3012, "Chercher dans le projet…", "Recherche un ticket dans le projet actuel.")
        subMenu301.Append(3013, "Tous les tickets", "Affiche une liste de tous les tickets du projet")

        subMenu302.Append(3021, "Chercher…", "Recherche un ticket dans tous les projets.")
        subMenu302.Append(3022, "Tous les tickets", "Affiche tous les tickets ouverts.")
        
        subMenu303.Append(3031, "Chercher…", "Recherche dans tous mes tickets.")
        subMenu303.Append(3031, "Chercher dans le projet…", "Recherche dans tous mes tickets.")
        subMenu303.Append(3032, "Tous mes tickets du projet actuel", "")
        subMenu303.Append(3033, "Tous mes tickets dans tous les projets", "")
        
        menu3.AppendMenu(301, "Projet en cours", subMenu301)
        menu3.AppendMenu(302, "Tous les projets", subMenu302)
        menu3.AppendMenu(303, "Mes tickets", subMenu303)
        
        menuBar.Append(menu3, "&Tickets")


        menu4 = wx.Menu()
        menu4.Append(401, "Documentation de ce projet…", "")
        menu4.Append(402, "Documentation de mon espace perso…", "")
        menuBar.Append(menu4, "&Documentation")
        
        menu5 = wx.Menu()
        menu5.Append(501, "Manuel", "Manuel d’utilisation d’Abeille")
        menu5.Append(502, "FAQ", "Foire Aux Questions")
        menu5.AppendSeparator()
        menu5.Append(503, "Signaler un problème…", "")
        menu5.AppendSeparator()
        menu5.Append(504, "À propos d’Abeille…", "")
        menuBar.Append(menu5, "&Aide")

        self.SetMenuBar(menuBar)
        
        self.Bind(wx.EVT_MENU_HIGHLIGHT_ALL, self.onMenuHighlight)
        self.Bind(wx.EVT_MENU, self.notDone, id=101)
        self.Bind(wx.EVT_MENU, self.notDone, id=102)
        self.Bind(wx.EVT_MENU, self.closeWindow, id=103)


    def onMenuHighlight(self, event):
        # Show how to get menu item info from this event handler
        id = event.GetMenuId()
        item = self.GetMenuBar().FindItemById(id)
        if item:
            text = item.GetText()
            help = item.GetHelp()

        # but in this case just call Skip so the default is done
        event.Skip() 

    def notDone(self, event):
        print('Not implemented yet!')

    def closeWindow(self, event):
        self.Close()
        

if __name__ == "__main__":
    app = Abeille(False)
    app.MainLoop()

