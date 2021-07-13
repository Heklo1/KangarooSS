from subprocess import Popen
import tkinter.messagebox
from time import mktime
import urllib.request
from tkinter import *
import subprocess
import datetime
import getpass
import hashlib
import ctypes
import random
import time
import sys
import os

ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def adminCheck():
    if is_admin():
        pass
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
        sys.exit()
################################# STRINGS2 DOWNLOAD ############################
url = 'https://github.com/glmcdona/strings2/raw/master/x64/Release/strings.exe'
username = getpass.getuser()
path = 'C:/Windows/Temp/strings2.exe'
latest = 'C:/Users/'+username+'/AppData/Roaming/.minecraft/logs/latest.log'
urllib.request.urlretrieve(url, path)
################################################################################

fullygone = [] # later use

def recordingCheck():
    softwares = ["bdcam.exe","action.exe","obs64.exe","dxtory"]
    found = []
    a = str(subprocess.check_output("tasklist")).lower()
    for software in softwares:
        if software in a:
            found.append(software)
    if len(found) > 0:
        msg = "=== Recording software found ==="
        for s in found:
            msg += "\n - " + s
        popUp("Recording Scan",msg)

def popUp(title, msg):
    ctypes.windll.user32.MessageBoxW(0, msg, title, 1)

def md5(string):
    return hashlib.md5(string.encode()).hexdigest()
def sapphireCheck():
    try:
        f = open("C:/Windows/Temp/strings2.exe",'rb')
        dump = str(f.read())
        f.close()
        if str(md5(dump)) in "e89e57b0b9ee2e7964ae45aeb8073488":
            return False
        else:
            return True
    except:
        return True

def dumpJavaw():
    os.system("cls")
    dumpcmd = 'for /f "tokens=2" %%a in (\'tasklist^|find /i "javaw"\') do ( @echo Dumping javaw.exe - %%a &&C:/Windows/Temp/strings2.exe -l 5 -pid %%a -raw )'
    b = open('C:/Windows/Temp/dump.bat', 'w')
    b.write('@echo off\n')
    b.write(dumpcmd + '\n')
    b.write('exit\n')
    b.close()
    if sapphireCheck():
        popUp("Kangaroo","Confirmed Anti-SS Tool Found")
        return 0
    strings = []
    try:
        p = str(subprocess.check_output(['C:/Windows/Temp/dump.bat']))
        strings = list(set(p.split("\\r\\n")))
    except:
        popUp("Kangaroo","Error: Unable to dump javaw!")

    if len(strings) > 100:
        dump = "\n".join(strings)
        versionInfo(dump)
        DCC(dump)
        if scanJavawStrings(dump) == 1:
            f = open("kangaroo_javaw.txt","w")
            f.write(dump)
            f.close()
    else:
        popUp("Kangaroo","Error: Minecraft not running")
    os.remove('C:/Windows/Temp/dump.bat')

def versionInfo(_dump):
    try:
        dump = _dump.split("\n")
        mcuser = "{Error}"
        f = open(latest)
        for line in f:
            if "Setting user: " in line:
                mcuser = line[line.index("Setting user: ")+14:]
        f.close()
        verline = ""
        for string in dump:
            if "--username" in string and "--version" in string:
                verline = string[string.index("--version ")+10:]
                break
        version = verline[:verline.index(" ")]
        popUp("Version Information [1/3]","USERNAME :: " + mcuser + "\nVERSION :: " + version)
    except:
        popUp("Version Information [1/3]","Error: Unable to determine username and/or version.")

def cstring(string):
    try:
        a= string[0:string.index(":_:")]
        return a
    except:
        return "ERR00039"

def cname(string):
    return string[string.index(":_:")+3:]

def scanJavawStrings(dump):
    combos = ['!"#&\',-.12367:;<=>GJQVXZ[_bdfhjkwy:_:Vape Lite #1 [BLC]', "&',-.12367:;<=>GJQVXZ[_bdfhjkwy:_:Vape Lite #2 [BLC]", 'java/lang/ref/Finalizer$1.class:_:Generic Autoclicker #1', 'RSDSg@{r:_:Skyfall Injection Client', 'vapelogo:_:Vape v3/4 #1', 'killaura-alloweditems:_:Vape v3/4 #2', 'aimassist-alloweditems:_:Vape v3/4 #3', 'double_click_enabled:_:Vape v3/4 #4', 'SqtkUVg:_:Vape v3 #1', 'CABzZzJ):_:Vape v3 #2', 'iReSqtkUVgAHOiReSqtkUVg:_:Vape v3 #3', 'erouax/instavape:_:Wax Vape Mod', 'com/sun/jna/z/a/e/a/a/a/f:_:Vape Cracked #1 [FORGE ONLY]', 'com/sun/jna/z/a/f/a/a/a/a/e/a/f:_:Vape Cracked #2 [FORGE ONLY]', 'manthe, aimassist:_:Vape Cracked #3', 'com.sun.jna.zagg:_:Vape Cracked #4 [FORGE ONLY]', '2.47-KILL:_:Vape Cracked #5 [FORGE ONLY]', 'yCcADi:_:Vape Cracked #7 [FORGE ONLY]', '>KRTal:_:Vape Cracked #8 [FORGE ONLY]', '*YXY*[:_:Vape Cracked #9 [FORGE ONLY]', 'kcc((k:_:Vape Variation #2 [FORGE ONLY]', 'C()[Lf/r;:_:Vape Variation #3 [FORGE ONLY]', '(ILjava/lang/Object;[S)V:_:Vape Variation #4', 'me.arabpvp.Reborn:_:ArabPvP Mod Client', 'me.Austin.client:_:Austin Mod Client', 'me.falconpenny.spclient:_:Falconpenny Mod Client', 'me.flame.emod:_:Flame Mod Client', 'me.fury.sdom.aa:_:ToggleChat Mod Client', 'me.iquintennn.paralyzed:_:IQuintennn Mod Client', 'me.jacobtread1.isync:_:Jacobtread1 Mod Client', 'me.Jailbreak:_:Jailbreak Mod Client', 'me.M4ssivo.togglesneak:_:M4ssiv0 Mod Client', 'me.peyote.client:_:Peyote Mod Client', 'me.protocol_client:_:Protocol Mod Client', 'me.salamander.client:_:Salamander Mod Client', 'me.somera:_:Somera Mod Client', 'me.tarasov:_:Tarasov Mod Client', 'me.thenexus.nexus:_:Nexus Mod Client', 'me.tigreax.nova:_:Tigreax Mod Client', 'me.zero.client:_:Zero Mod Client', 'hakery.c:_:Latemod Injection Client #1', 'hakery.club:_:Latemod Injection Client #2', ';9<C7D=CHCAL>@?DQI;MDSQRNQIMKEJ8:_:Drip Cracked #1', "E-6%%&>6C(\\'<=7BR*$*+*:_:Drip Cracked #2", '0,$037ADCBDIJICA:_:Drip Cracked #3', 'ZKM9.0.2:_:Zelix Klassmaster Obfuscation', 'Zkh}e:_:Demon Injection Client #2', '_o&`EGDIk0,AK:_:Demon Injection Cracked', 'net/minecraft/lIlIllIIlIIIllIllI/IlIlllIIlllIIIIllI.class:_:Labymod Client #1', 'LabyMod_nngskjgkjsbkljsblkfblfbslk:_:Labymod Client #2', 'LabyMod_nngskjgkjsbkljsblkfblfbslk/:_:Labymod Client #3', 'de.labymod.client.modules.impl.AimAssist:_:Labymod Client #4', 'de/labystudio/utils/me/jannik/module/Module.class:_:Labymod Client #5', 'me/azoq/azoq.class:_:Labymod Client #6', 'me/azoq/ui/Main$1.class:_:Labymod Client #7', 'LabyMos V7 | By JensDE:_:Labymod Client #8', 'LabyModClient - By ViTox:_:Labymod Client #9', 'LabyMod_sjfksnbdslkdnbcnklnvcm:_:Labymod Client #10', 'io/fishermen/fpsdisplay/settings/Dada.class:_:Grim Mod Client #2', 'fishermen/fpsdisplay/hehe.class:_:Grim Mod Client #3', 'b/mods/combat/:_:Grim Mod Client #4', 'Bruvv.LOL.M:_:Grim Mod Client #5', 'Py3ss 4 k3y:_:Grim Mod Client #6', 'Module3/a:_:Grim Mod Client #7', 'Ranked Skywars  -BEST WISHES FROM BRUVV :):_:Bruvv Mod Client #1', 'me.Bruvv:_:Bruvv Mod Client #2', '%01%01%01%01%01%01%01%01.class:_:Authority Mod Client', 'net.reach.Verzide:_:Verzide Reach Mod #1', 'net\\reach\\Verzide:_:Verzide Reach Mod #2', 'reach/Verzide:_:Verzide Reach Client #3', 'me/tsglu/ke/HitBoxCommands:_:TSGLuke Client #1', 'me/tsglu/ke:_:TSGLuke Client #2', 'me.tsglu.ke.:_:TSGLuke Client #3', 'Hitbox Multiplier set to: :_:TSGLuke Client #4', 'io.conceal:_:Conceal Injection Client', 'me/tyler/util/CombatUtil.class:_:Tyler Client', 'cunt faggot adopted clapped fumed hoe Client:_:cunt faggot adopted clapped fumed hoe Client', 'assets/minecraft/Deepwe.png:_:God Mod Client', 'trumpclientftw_:_:Bape Mod Client #1', 'Bape_g:_:Bape Mod Client #2', '<>ZRX44:_:Trump Client #1', '580wxfgyi5r423kdwsnmxdca66cr5k91j1swslizpd6a1vyk2t1ck5iaapzedh6j5u2nqcf36y7fkmx8i2gc01kr973j38obnkk:_:Trump Client #2', 'xyz/Incide/gui:_:Incide Client', 'assets/minecraft/ace/cape.png:_:Ace Version Client', 'Cracked by rigole, enjoy your skid:_:Onyc Client #1', '%e2%80%81%e2%80%89%e2%80%85%e2%80%87.class:_:Onyc Client #2', 'purgeclient/purgeclientD:_:Purge Client #1', '\\\\Wbem\\\\wmic.exe:_:Purge Client #2', 'me.veylkar.pepe:_:Pepe Mod Client #1', 'me/veylkar/pepe:_:Pepe Mod Client #2', 'me/veylkar/pepe/modes/ModeSprint:_:Pepe Mod Client #3', 'us/cuck/core/module/modules/combat/:_:Cyanide Injection Client #1', '.us.cuck.core.module.modules.combat.AutoClicker:_:Cyanide Injection Client #2', 'CyanideButtonUI.java:_:Cyanide Injection Client #3', 'Injected into minecraft enjoy cheating you cuck:_:Cyanide Injection Client #4', 'Cyanit/ab.class:_:Cyanide Skid', 'bspkrs/bspkrscore/fml/UncommonProxy.classUT:_:Bspkrscore Mod Client #1', 'bspkrs/bspkrscore/fml/ProxyPool.classUT:_:Bspkrscore Mod Client #2', 'fml/bspkrsCoreMod$1.classUT:_:Bspkrscore Mod Client #3', 'bspkrs/NigLoad:_:Bspkrscore Mod Client #4', 'pw/cinque/keystrokesmod/MouseButton$1.class:_:KeystrokesMod Cheat #1', 'pw/cinque/keystrokes/KeystrokesMod.classUT:_:KeystrokesMod Cheat #2', 'keystr0kes/UT:_:Raven Mod Client #1', 'R4V3NR4V3NR4V3NR4V3NR4V3ND2:_:Raven Mod Client #2', 'pw/cinque/keystrokesmod/render/AwhhShitHeFuckedUp.classUT:_:KeystrokesMod ASHFU Client #1', 'AwhhShitHeFuckedUp.classUT:_:KeystrokesMod ASHFU Client #2', 'AwhhShitHeFuckedUp.java:_:KeystrokesMod ASFHU Client #3', 'Minecraft 1.7.10 | R::_:KeystrokesMod/BSP Reach #1', 's | T::_:KeystrokesMod/BSP Reach #2', '.1f | AC::_:Keystrokes/BSP Mod Reach #3', 's | AA::_:Keystrokes/BSP Mod Reach #4', 'mobambaclient.jar:_:Mo Bamba Client', 'ping:textures/ping.png:_:AntiKB Mod #1', 'knockback.setvalue:_:AntiKB Mod #2', 'dos\\rapidity\\knock:_:AntiKB Mod #3', 'velocity/tcpLat:_:AntiKB Mod #5', 'dmillerw/ping:_:AntiKB Mod #6', 'KB/op13/ping:_:AntiKB Mod #7', 'KBMOD.class:_:AntiKB Mod #8', 'KBMOD.java:_:AntiKB Mod #9', 'Lemonade v1.8:_:Lemonade Injection Client', '!/fastcraft/m.class:_:Fusk Mod Client #1', '!/fastcraft/L.class:_:Fusk Mod Client #2', '(Lfastcraft/c;)V:_:Fusk/HR Mod Client #3', 'hi\\f\\A.class:_:Fusk/HR Mod Client #4', 'n%\\u0007La:_:Fusk Mod Client #1', 'oG]DVD]:_:Fusk Mod Client #2', 'QbmWxU:_:Fusk Mod Client #3', 'jdGyW`!z@:_: Fusk Mod Client #4', 'kyprak.agent:_:Kyprak Injection Client #1', 'Kyprak.jar:_:Kyprak Injection Client #2', 'xyz/gucciclient/modules/UT:_:Gucci Mod Client #1', 'gucci.java:_:Gucci Mod Client #2', 'G0ttaDipMen.java:_:Gucci Mod Client #3', 'me/massi/reach:_:Massi Reach Mod #1', 'me.massi.reach:_:Massi Reach Mod #2', 'io/fishermen/fpsdisplay/settings/Ve.class:_:FpsDisplay Cheat', 'assets/directionhud/textures/gui/compass1.class:_:DirectionHUD Reach Mod #1', 'directionhud/textures/gui/icon.class:_:DirectionHUD Reach Mod #2', 'me/dewgs/particlemod/ParticleMod$1.class:_:ParticleMod Client', 'BetterStrafe.class:_:OmniSprint Client', 'pw/cinque/motionblur/commands/CSunS:_:MotionBlur Misplace', '+(M0G.V:_:Hillary Rodham Mod Client', 'apeya}l`|<?IAER:_:Hillary Rodham Mod Client', 'r8C*E:_:Hillary Rodham Mod Client', 'luqx?$~cg:le:_:Hillary Rodham Mod Client', '/keystrokes/pp/Willy:_:Willy Ghost Client #1', 'sWilly.java:_:Willy Ghost Client #2', 'pw.cinque.keystrokes.pp.mod.all.Gui:_:Willy Ghost Client #3', '(IIFFFFFFFF)V:_:Willy Ghost Client Skid [FORGE ONLY]', 'fitchi.agent:_:Fitchi Injection Client', 'pww/cinque:_:Illegitimate Mod Signature', 'net/minecraft/client/e/MASLJ:_:MASLJ Client', 'net.azurewebsites.thehen101.gc:_:TheHen101 Cheat (lol)', 'UniqueAntiLeak/:_:Unique Client #1', 'Unique/Unique0.class:_:Unique Client #2', 'config/Unique:_:Unique Client #3', 'che4tlogprivcli3nt:_:Universe Injection Client', 'FullTolerance.jar:_:FullTolerance (Anti SS Tool?)', 'kappa_KappaClient_:_:Kappa Client #1', 'KappaClient Detectors:_:Kappa Client #2', '/ss [Strafe Multiplier]:_:Strafe Multiplier', 'net/kohi/tcpnodelaymod/aux:_:Vea mod client #1', 'net/kohi/tcpnodelaymod/a.classPK:_:Vea Mod Client #2', 'net/kohi/tcpnodelaymod/nul:_:Vea Mod Client #3', 'net/kohi/tcpnodelaymod/cON:_:Vea Mod Client #4', 'kohi/tcpnodelaymod/Prn:_:Vea Mod Client #5', 'kohi/tcpnodelaymod/AuX.class:_:Vea Mod Client #6', 'kohi/tcpnodelaymod/cON:_:Vea Mod Client #7', 'kohi/tcpnodelaymod/J.class:_:TCPNoDelay Cheat #1', 'net/kohi/tcpnodelaymod/255.0:_:TCPNoDelay Cheat #2', 'kohi\\tcpnodelaymod\\ServerProxy:_:TCPNoDelay Cheat #2', 'kohi\\\\tcpnodelaymod\\\\ServerProxy:_:TCPNoDelay Cheat #3', 'ASM: net.kohi.tcpnodelaymod.:_:TCPNoDelay Cheat #4', 'net/kohi/tcpnodelaymod/Proxy.class:_:TCPNoDelay Cheat #5', 'tcpnodelaymod/IModGui:_:TCPNoDelay Cheat #6', 'net/rebellion/tcpnodelaymod/Main.class:_:TCPNoDelay Cheat #7 (Rebellion)', 'kohi/tcpnodelaymod/Tweaker:_:TCPNoDelay Cheat #8', 'TcpNoDelayTweaker.classUT:_:TcpNoDelay Cheat #9', 'Better Strafe Mod By Cheeky/Koupah:_:Koupah Client #1', 'koupah.Main:_:Koupah Client #2', 'Koupah/is/:_:Koupah Client #3', 'IngameAccountSwitcher$1.class:_:InGame Account Switcher', 'me/stoud/merge/End:_:Merge Client #1', 'me/stoud/merge/HWIDUtils:_:Merge Client #2', 'a/IiIiiIIIIi:_:Merge Client #3', 'i[JQQI:_:Merge Client #4', 'YTQBFIXVF:_:Merge Client #5', 'Aimbot: False:_:Merge Aimbot', 'me/rigamortis/faurax/Timer.class:_:Rigamortis Client', 'net/minecraft/tmih/utils/Timer.class:_:Timih Mod Client #1', 'me.tmih.ac:_:Timih Mod Client #2', 'omikronclient.com:_:Omikron Client #1', 'd[>L6:_:Xanax Client or Canalex Keystrokes Client', 'kiedHdNT>Z<RI:_:Canelex Keystrokes Client #2', '41/41/41/8/41:_:Magenta Mod Client #1', 'avatarhasautisminthehead:_:Magenta Mod Client #2', 'acs/tabbychat/injection:_:Spooky Caspar Ghost Client', 'io/fishermen/fpsdisplay/settings/Wool.class:_:CheatbreakerHUD Cheat', 'necrum/Main.class:_:Necrum Client', 'kys/bleach/Bleach:_:Bleach Client', 'Cracked by Buddy [SirJava]:_:SirJava Crack Signature', 'pw/cinque/cpsmod/SpoofType.class:_:CPSmod Spoofer', '&.EGO\\^`ijnoz|:_:Wet Noodle', 'pw/latematt/xiv/value/ClampedValue.class:_:Latematt Client', '10/10/80/41:_:Kurium Injection Client', '/cpsmod/settings/Utility.class:_:CPSMod Client', '.onetap.cc:_:OneTap Client #1', '_/true:_:OneTap Client #2', '_/iffinal.class:_:OneTap Client #3', 'lemon.the.pvper.wrapper:_:Lemon Injection Client', 'durtaog/com/sun/jna:_:Durtaog Client #1', 'durtaog/client:_:Durtaog Client #2', 'xyz/Grand0x/gui:_:Grand0x Client #1', 'FREE/Grand0x:_:Grand0x Client #2', 'GHOSTBYTES - CRACKED BY GRAND0X:_:Ghostbytes Grand0x Leak', 'fucked by 0x22:_:0x22 Leaked Client', 'Cracked by 0x22:_:0x22 Cracked Client', 'Cracked by Buddy:_:Buddy Cracked Client', 'Cracked By Grand0x:_:Grand0x Cracked Client', 'Cracked by rigole:_:Rigole Cracked Client', 'cracked by shitkid:_:Shitkid Cracked Client', 'Cracked by Syn:_:Syn Cracked Client', 'Cracked by Ygore:_:Ygore Cracked Client', 'Cracked by: H&E:_:H&E Cracked Client', 'Veiv Client - WATERMARK:_:Veiv Client', 'me/billybob1060/reflex/init/guis/GuiLoading:_:Reflex Client #1', 'me.billybob1060.reflex.Reflex:_:Reflex Client #2', 'DoubleClicker.class:_:Double Clicker', '"particlemod/ParticleMod$1.class");:_:ParticleMod Cheat', 'OLaperture/module/ModuleManager;:_:Aperture Client', 'batty/ui/server/ServerProxy:_:Batty Coordinates Cheat', 'Phoenix/Modules:_:Phoenix Hacked Client', 'pww/cinque/timechanger/:_:TimeChanger Cheat', 'pw/cinque/timechanger/commands/CommandFastTime.classUT:_:Possible TimeChanger Misplace #1', 'src/PK?:_:Possible Timechanger Misplace #2', 'TimeType.classUT:_:Possible TimeChanger Misplace #3', 'src/a.class:_:Possible TimeChanger Misplace #4', '([SSl)Z:_:OCMC Reach', 'mincpsEST.MF:_:AutoClicker Configuration', 'C;rR.y_pt-n0gT^YCX@:_:Crypt Client', 'Syphlex Forge.jar:_:Syphlex Client', 'FuncraftDelay:_:Funcraft Client', 'prinnce/:_:Way Client', 'DELIX_SKIDPROTECT:_:Delix Client', 'sallos/Sallos:_:Sallos Client', 'batty/ui/server/ServerProxy.class:_: Batty Reach Mod', 'me/tojatta/clicker:_:Tojatta Clicker #1', 'me.tojatta.clicker:_:Tojatta Clicker #2', 'Pandora\\Modules\\Combat:_:Pandora Version Client', 'PandoraIsAMinecraftCheat:_:Pandora Version Client', 'maven/harambe/:_:Harambe Injection Client #1', 'harambe.png:_:Harambe Injection Client #2', 'META-INF/maven/harambe/Harambe/:_:Harambe Injection Client #3', 'BetterStrafe.java:_:OmniSprint Mod', 'assets/minecraft/flare:_:Flare Version Client', 'Triggerbot delay (MS randomized):_:ToggleSneak Hack', 'SSROCK_Velocity:_:Regedit Mod Cheat', 'me/aristhena/event/events/TickEvent.class:_:Avix (Fade) Client #1', 'me/aristhena/event/events/StepEvent.class:_:Avix (Fade) Client #2', 'me.aristhena:_:Avix (Fade) Client #3', 'Sallos_By_Soirr:_:Sallos Client', 'xray/bypass/XRay$1:_:Xray Mod Client', 'dg82fo.pw:_:Drek Client', 'azurewebsites/:_:Azure Client', 'br/alkazuz/ircTwitterLogger.class:_:Alkazuz Client', 'BirkenFosegeTunchtEnemvertReibenzUeidaKerLeinEzehNhEihutdASZ.class:_:Nein German Client', 'spook:sword.png:_:Spook Client', 'leakforums.net.user665158.modules.SmoothAimbot:_:Leakforums Client', 'net\\latency\\speed\\ArtLatencyTw.class:_:Ping Spoofer Mod', 'ZnVuY18:_:Drek Client', '/s/%e2%80%8d%e2%80%8d%e2%80%89%e2%80%8a.class:_:Skilled Client #1', 'assets/minecraft/watermPK:_:Skilled Mod Client #2', 'assets/minecraft/0adjkfh31PK:_:Skilled Mod Client v2 #1', 'skilleddabful:_:Skilled Mod Client v2 #2', 'net.wurstclient.gui.main:_:Wurst Version Client', 'data/maxou:_:Maxou Client', 'lemon/the/pvper/mods:_:Lemon Injection Client', 'Hacks/modules/KillAura$1.class:_:Specific KillAura Class', 'lsdclicker.xml:_:LSD Clicker', 'spook/autoclicker.png:_:Spook Client', 'assets/minecraft/flux/:_:Flux Client', 'mods/togglesneak/proxy/Proxy3bkq$1$1.class:_:ToggleSneak Cheat', 'our/mod/asparagus:_:Asparagus Mod Client', 'Triggerbot [G]:_:G Client', 'me/dewgs/particlemod/x/FakeMeFraClass123456:_:Dewgs ParticleMod Cheat', '5KPoq:_:Wet Noodle', 'net/frozenorb/h2c/Clickhold.class:_:Ethylene Mod Client #1', 'me.ethan.ethylene:_:Ethylene Mod Client #2', 'Ethylene.jar:_:Ethylene Mod Client #3', 'priority/hit/range/:_:Priority Reach Mod', 'fr/reizam/deiramod/mods/Reach.java:_:Reizam Reach Mod', 'deez/togglesneak/ForgeLoader:_:ToggleSneak Cheat', 'mcmodding4k/fastbridge/:_:FastBridge Mod', 'tsissAmiA:_:Syntax Client', 'mousetweaks/Mousebutton.c:_:MouseTweaks Cheat', 'textures/Hekate/bg:_:Hekate Version Client', 'LSquad.dll:_:String Cleaner', 'net/azurewebsites/thehen101/gc/mod/Triggerbot.class:_:TheHen101 Client lol', 'net/Cancer/ProxyClient:_:Cancer Client', 'deez/togglesneak/era/mod/mods/Velocity.class:_:ToggleSneak Cheat', 't/z/q/q.class:_:Huume Mod Client #1', 'm/y/o/o/r.class:_:Huume Mod Client #2', '3telltalegames.batmanthetelltaleseries_4p9dzwrngadje:_:Batman Client', 'cane8993jdsjad98sad9ssa9.altervista.org:_:Casper Injection Client', 'gorilla/Gorilla.class:_:Gorilla Injection Client #1', 'gorilla/gui/component/GuiToggle:_:Gorilla Injection Client #2', 'gorilla/Agent:_:Gorilla Injection Client #3', 'GorillaGlue.java:_:GorillaGlue Client', '(Sll)S:_:OCMC Reach #2', 'ml/rederpz/sync/friend/FriendManager.class:_:Rederpz Mod Client #1', 'me.rederpz.haste:_:Rederpz Mod Client #2', 'mousetweaks/liteloader/LiteModMouseTweaks:_:MouseTweaks Cheat', 'me/tmih/yt/AC.class:_:Tmih Autoclicker', 'winter/utils/Player.class:_:Winter Client', 'me.tyler.module.mods.Criticals:_:Tyler Client', 'Autoclicker Toggle: Alt:_:Tap Client Autoclicker', 'maxcpsEST.MF:_:Generic Autoclicker', 'xyz/Grand0x/m0dules:_:Grand0x Client', 'leakforums.net.user665158.modules:_:Leakforums Client', 'deez/togglesneak/ToggleEventsMod:_:ToggleSneak Cheat', 'ASM: pw.cinque.cpsmod.CPSMod:_:CPSMod Cheat', 'onetap.cc:_:OneTap Cheat', 'assets/minecraft/wolfram/bg-blur.jpg:_:Wolfram Client', '„é?³.class:_:That weird ass symbols client', 'phantom\\modules.properties:_:Phantom Version Client #1', 'combat/EntityKiller:_:Phantom Version Client #2', 'PhantomClient.java:_:Phantom Version Client #3', 'Aimboat.class:_:Phantom Version Client #4', 'b.mods.combat:_:Phantom Version Client #5', 'Prevents Killaura from attacking teammates.:_:Specific KillAura', 'xyz/Grand0x/gui/component/Frame:_:Grand0x Client', 'pw/cinque/motionblur/TT:_:MotionBlur Cheat', 'hi.a2:_:Veiv Injection Client #1', '(Lhi/aK;ILhi/Q;)V:_:Veiv Injection Client #2', 'hi\\f\\A.class:_:Veiv Injection Client #3', ': isAimbotEnabled:_:Specific Aimbot', "144.217.87.106:_:Zuiy's IP", '_________â€:_:Another Weird Ass Symbols Client', 'future/api:_:Future Client #1', 'io.futurehack:_:Future Client #2', "Injected Successfully, Cracked by dinkIO ;-) you suck fyu don't make clients:_:Some FYU Cheat", '"IQLw:_:Misplace Mod', 'me/cupboard/command/Command.class:_:Cupboard Mod Client #1', 'me.cupboard:_:Cupboard Mod Client #2', 'me/dewgs/particlemod/ParticleMod$1:_:Dewgs ParticleMod Cheat', 'CancerTweaker.class:_:Cancer Client', 'SkidProtection/:_:Skid Obfuscation', 'mousetweaks/IGuiScreenHandler:_:MouseTweaks Cheat', "me/rowin/destruct:_:Rowin's Client", 'liquidbounce/taco/1.png:_:LiquidBounce #1', 'META-INF/byCCBlueX/LiquidBounce/:_:LiquidBounce Mod Client #1', 'net.ccbluex.LiquidBounce.injection.mixins.MixinBlockLadder:_:LiquidBounce Injection #2', 'tk/ccbluex/LiquidBounce/injection/mixins/MixinGuiButton.class:_:LiquidBounce Injection Client #3', 'ccbluex/LiquidBounce:_:LiquidBounce Injection Client #4', 'CRACKED  BY FUSKED:_:Fusked Crack', 'bmV4dEVsZW1lbnQ=:_:Drek Client', 'assets/minecraft/huzuni/title.png:_:Huzuni Version Client', 'IIiIIiIiIiiiIiIiIiiI:_:Spook Cracked', 'zerodayboi/C:_:ZeroDay Client', 'net.Cancer.ProxyClient:_:Cancer Client', 'deez/togglesneak/era/mods/Triggerbot:_:Togglesneak Cheat', '#*Z#%*Z#:_:Wet Noodle', 'reachmod/ReachMod.class:_:Reach Mod', 'particlemod/ParticleMod$1.class");:_:Particle Mod Cheat', 'lee0xp28dd2c7955ce926456240b2ff0100bde9b51b4e0f250230de20e3e15cece6efa:_:Smoke Client', 'ALLATORIxDEMO:_:Allatori Obfuscation #1', "Obfuscation by Allatori Obfuscator http://www.allatori.com':_:Allatori Obfuscation #2", 'yalter/mousetweaks/loaders/MouseTweaksForge:_:MouseTweaks Cheat', '1.8-Optifine_HD_U_H4:_:Some Fake Optifine I think', 'a/a/a/OO000O00O0O00OO:_:XTC Client', 'Bon mot de passe =):_:Some French cheat (idk the name)', '!/fastcraft/M.class:_:Fusk Mod Client #1', '!/fastcraft/b.class:_:Fusk Mod Client #2', '!/fastcraft/d.class:_:Fusk Mod Client #3', 'assets/metro/fonts:_:Metro Version Client #1', 'assets/metro/:_:Metro Version Client #2', 'METRO CLIENT:_:Metro Version Client #3', '/Metro5.1.jar:_:Metro Version Client #4', 'ReachMod.java:_:Reach Mod', 'me/javlin/sharpnessparticles/SharpnessParticles3.classPK:_:Javlin Mod Client', 'hypixel/xray/bypass/XRay$1:_:Hypixel Xray Mod', 'me.tyler.module.mods:_:Tyler Mod Client', '/ae$$Lambda:_:Bit Injection Client', 'net/minecraftxray:_:Xray Mod', 'our.mod.asparagus:_:Asparagus Mod Client', 'incogntoc:_:Incognito Injection Client #1', 'czaarek99/:_:Incognito Injection Client #2', 'mojang/craft/block/w0mb4t/ac$m:_:W0mb4t Client', 'aperture/module:_:Aperture Client', 'me/zero/clarinet/Impact.class:_:Zero Client', 'bray/Axis:_:Bray Client', 'io/netty/bestclient/:_:Best Client', 'Freestyler/Tweaker.class:_:FreeStyler Client', 'buddy/Hijacked:_:Buddy Client', 'net.Krypton.UI:_:Krypton Mod Client', 'durtaog/client:_:Durtaog Client', 'Main8888:_:Main8 Client', 'EaZy/MainMenu/:_:EaZy Client', 'Small_Cheat:_:Small Client', 'science/roblox/latch/plugin/plugins/combat/Forcefield:_:Roblox Client (for minecraft)', 'the_fireplace/fluidity:_:Fluidity Client', 'glockteam:_:Glock Client', 'Minestrike/Cops & Crims ragebot.:_:Ragebot Client', 'stats/settings/shark:_:Mushway Client', 'me/aarow/:_:Arrow Client', 'Yay_Logo.png:_:Yay Client', 'legacy/gui/C:_:Legacy Client', 'libs.poisonex.nematode:_:Poisonex Injection Client', 'SpicyPauls:_:Spicy Paul Client', 'leonhard08kl1156126403715:_:Adrigoron Client', 'me/yario/fakegui:_:Yario Client', '/frozenorb/:_:FrozenOrb Cheat', 'net/prinnce/wayclient/EventMod:_:Way Client', 'SAINTCLIENT:_:Saint Client', 'FakeYticolevClass123456.:_:Skuuunksle100 Client #1', 'FakeDestructelsfClass123456:_:Skuuunksle100 Client #2', 'supercheese200:_:Cheese Client', 'hasureclient:_:Hasure Client', 'de/Garkolym/HackedItem.class:_:Garkolym Client', "johny9020_:_:Johny's Client", 'Horizon/Trism/:_:Horizon Client', 'me/ygore/clint/Client.javaUT:_:Ygore Mod Client', 'me/raizex/ancient/module:_:Raizex Client', 'WomboClient\\\\WomboClient:_:Wombo Client', 'com/S9_/:_:SNINE Client', 'net/prinnce/wayclient:_:Way Client', 'net/minecraft/l/b/Obscure/p:_:Obscure Client #1', 'set->Killaura-Invis-false;:_:Obscure Client #2', 'dezztroy:_:Possible Dezz Troy Client', 'minecraft/textures/gui/bg2:_:BG2 Client', 'sl/steeldood/bit/client/module/impl/combat/ModuleAutoclicker:_:SteelDood Client', 'AtomClient4Beta:_:Atom Client', 'paralyzed.module.modules:_:Paralyzed Client', 'zues/AltManager:_:Zues Client', 'SamerDEV%20Sub%20me:_:SamerDev Client', 'fr/reizam/deiramod/mods/Reach.class:_:Reizam Client', 'skillclient-logo.png:_:Skill Client', 'rupture/gui/aquaGui/RuptureClickGui.class:_:Rupture Client', 'Youre_Watching_Brazzers_:_:Porn Client', 'gui/rekt:_:Rekt Client', '/rogers/alaska:_:Alaska Client', 'children/Gui:_:Children Client', 'yellowlight2:_:Yellow Light Client', 'me/tru3/base/modules/ModuleManager:_:Krypto B1 Client', 'porkchop_ERA:_:Porkchop Client', 'me/ygore/clint/Client.classUT:_:YGORE CLINT CLIENT', 'AVClientTrig:_:AV CLient', 'net/aristois/opencode/:_:Aristois Mod Client #1', 'me.deftware.aristois:_:Aristois Mod Client #2', '/provida/:_:Provida Client', 'package./caden/:_:Chilli Caden Client #1', '0X71756747815855352521535263565341:_:Chilli Caden Client #2', 'caden/modules/:_:Chilli Caden Client #3', 'Aperture.class:_:Aperture Client', 'perocent/:_:Perocent Client', 'net/minecraft/scooby/util/ModeUtils.class:_:Scooby Client', 'me/Austin/client/modules:_:Austin Client', 'RapeClient:_:Rape Client', 'Xerxes.jar:_:Xerxes', 'BITCHESS45:_:Bitchess45 Client', '7.modulelist:_:Seven Client', '/wenzys/:_:Wenzys Injection Client #1', 'io.wenzys:_:Wenzys Injection Client #2', 'AutoClicker.properties:_:Generic Config Clicker #1 ', 'clicker/setvalue:_:Generic Config Clicker #2', 'clicker.setvalue:_:Generic Config Clicker #3', 'optionspvp.txt:_:Generic Config Combat', 'xray.cfg:_:Generic Config X-Ray #1', 'XRay.properties:_:Generic Config X-ray #2', 'isAimbotEnabled:_:Generic Config Aimbot #1', 'aimbot_range:_:Generic Config Aimbot #2', 'Aura_range:_:Generic Config Reach', 'Triggerbot_delay:_:Generic Config Triggerbot', 'modules/AutoClicker:_:Generic Module AutoClicker', 'modules/ForceField:_:Generic Module ForceField', 'modules/KillAura:_:Generic Module KillAura', 'modules/SmoothAim:_:Generic Module SmoothAim', 'modules/Velocity:_:Generic Module Velocity', 'modules/Aura.class:_:Generic Module Aura', 'mods/Range.class:_:Generic Module Range', 'mods/combat/:_:Generic Module Combat', 'autoclicker.class:_:Generic Class Autoclicker', 'PingSpoof.class:_:Generic Class PingSpoof', 'ReachMod.class:_:Generic Class Reach', 'AntiVoid.class:_:Generic Class AntiVoid', 'XRay.class:_:Generic Class Xray', 'aimbot.class:_:Generic Class Aimbot', 'TriggerBot.class:_:Generic Class Triggerbot', 'ChestStealer.class:_:Generic Class ChestStealer', 'SmoothAimbot.class:_:Generic Class SmoothAimbot', 'ForceField.class:_:Generic Class ForceField', 'AutoArmor.class:_:Generic Class AutoArmor', 'AimAssist.class:_:Generic Class AimAssist', 'reach/Reach.class:_:Generic Class Reach', 'AutoPearl.class:_:Generic Class AutoPearl', 'autoclicker.java:_:Generic Java Autoclicker', 'DoubleClicker.java:_:Generic Java DoubleClicker', 'CombatUtil.java:_:Generic Java CombatUtil', 'ChestStealer.java:_:Generic Java CheatStealer', 'AutoArmor.java:_:Generic Java AutoArmor', 'PingSpoof.java:_:Generic Java PingSpoof', 'AutoPearl.java:_:Generic Java AutoPearl', 'PacketMode.java:_:Generic Java Packet', 'aimbot.java:_:Generic Java Aimbot', 'TriggerBot.java:_:Generic Java Triggerbot', 'ExtendedReach.java:_:Generic Java Reach', 'SmoothAimbot.java:_:Generic Java SmoothAimbot', 'XRay.java:_:Generic Java X-Ray', 'AimAssist.java:_:Generic Java AimAssist', 'ForceField.java:_:Generic Java ForceField', 'AntiVoid.java:_:Generic Java AntiVoid', 'AimbotGui.java:_:Generic Java Aimbot', 'KillAura.java:_:Generic Java KillAura', 'combat/AutoClicker:_:Generic Combat Clicker', 'combat/KillAura:_:Generic Combat Aura', 'combat/Aura:_:Generic Combat Aura #2', 'combat/Velocity:_:Generic Combat Velocity', 'combat/SmoothAim:_:Generic Combat SmoothAim', 'combat/Hitbox:_:Generic Combat Hitboxes', 'combat/Reach:_:Generic Combat Reach', 'combat/AimAssist:_:Generic Combat AimAssist', 'net/minecraft/entity/Entity.classPK:_:Generic Misplace #1', 'NBTMultipart.class:_:Generic Misplace #2', 'MCNetHandler:_:Generic Misplace #3', 'TcpAck:_:Generic Misplace #4', 'TCNH$1:_:Generic Misplace #5', '-KillSwitch is enabled, program will shutdown.:_:Generic Self Destruct #1', 'Self-Destructed successfully.:_:Generic Self Destruct #2', 'SelfDestruct.class:_:Generic Self Destruct #3', 'SelfDestruct.java:_:Generic Self Destruct #4', '7selfDestruct:_:Generic Self Destruct #5', 'imgui_log.txt:_:Generic ImGUI', 'instrument.dll:_:Confirmed Injection Client #1 [FORGE ONLY]', 'shell.rundll32:_:Confirmed Injection Client #2 [FORGE ONLY]', 'InjectionDLL.dll:_:Bee Clicker Injection']
    cheats = []
    for combo in combos:
        if cstring(combo) in dump:
            cheats.append(cname(combo))
    if len(cheats) == 0:
        popUp("Javaw Scan [3/3]","User Clean!")
    else:
        msg = "=== Possible Cheats Found ["+str(len(cheats))+"] ==="
        for name in cheats:
            msg += "\n- " + name
        popUp("Javaw Scan [3/3]",msg)
    choice = yesno("Would you like to save the dump to a text file?")
    return choice        

def isSketchy(blegh):
    exe = blegh.replace(".exe","")
    info = getInfo(exe)
    vows = info[0]
    cons = info[1]
    lets = info[2]
    nums = info[3]
    upps = info[4]
    lows = info[5]
    size = info[6]
    one = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    two = "1234567890"
    try:
        sketchiness = 0
        for i in range(size-1):
            if exe[i] in one and exe[i+1] in two:
                sketchiness = 5
        if abs(0.50-upps/size) < 0.1 or ((upps>1) and (upps<size/2)):
            sketchiness += 2
        if abs(0.29-nums/size) > 0.1 or (nums<1):
            sketchiness -= 0.5
        if lets > 0:
            if abs(0.77-cons/lets) > 0.07:
                sketchiness -= 1
        if getGrams(exe) < 3:
            sketchiness += 2
        blacklist = ["64","32","86"," ","_",".","+","-","Svr","PnkB","strA","Reg","hell","Mc","comp","Comp","DAX3","ient","QcShm","MVsInst","Detect","MfeAVSvc","pkg","Pkg","srv","Srv","NordVPN","MSTest","VaultCmd","TFSBuild","MpUXSrv","TSWbPrxy","MSBuild","MpCmdRun","GfxUIEx","NvTmRep","VSPerfSrv","DXCap","NisSrv","DXCpl","BlueJ","RpcPing","MsPdbCmf","WpcMon","MdSched","BdeUISrv","WinMgmt","BdeHdCfg","SrTasks","hpPE","WmsSvc","RTFTrack","WpcTok","MsiDb","DW20","WmiApSrv","MsMpEng","VSPerf","SyncHost","SshSftp","NvTmMon","RmClient","SndVol","TlbImp","LaunchTM","VSPerfCmd","TlbExp","PkgMgr","SMSvcHost","MsiMsp","TsWpfWrp","Winrt2Ts","PrintBrm","igfxSDK","ChCfg","MdRes","RegSvcs","VsGa","FxCopCmd","TB3x","RdpSa","fltMC","CastSrv","LxRun","WMSvc"]
        
        for nope in blacklist:
            if nope in exe:
                sketchiness = 0
        if (size-lets-nums) > 0:
            sketchiness = 0
        if exe not in blacklist: 
            if sketchiness > 2:
                return 1
            else:
                return 0
        else:
            return 0
    except:
        return 0

def getGrams(exe):
    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"
    grams = 0
    pos = 0
    size = len(exe)-1
    while pos < size:
        if (exe[pos].lower() in vowels and exe[pos+1].lower() in consonants) or (exe[pos].lower() in consonants and exe[pos+1].lower() in vowels) or (exe[pos].lower() in vowels and exe[pos+1].lower() in vowels):
            grams += 1
        pos += 1
    return grams

def getInfo(exe):
    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"
    numbers = "1234567890"
    letters = "aeioubcdfghjklmnpqrstvwxyz"
    vows = 0
    cons = 0
    nums = 0
    upps = 0
    lows = 0
    lets = 0
    pos = 0
    size = len(exe)
    for char in exe:
        if char in vowels:
            vows += 1
        elif char in consonants:
            cons += 1
        if char.lower() in letters:
            lets += 1
        elif char in numbers:
            nums += 1
        if char.isupper():
            upps += 1
        elif char.islower():
            lows += 1
    return [vows,cons,lets,nums,upps,lows,size]

def getPIDs():
    a = str(subprocess.check_output("tasklist /svc /FI \"IMAGENAME eq svchost.exe\"")).split("\\r\\n")
    w = [0,0,0]
    for string in a:
        if string[35:39] == "DPS ":
            w[0] = str(int(string[11:34]))
        if string[35:45] == "DiagTrack ":
            w[1] = str(int(string[11:34]))
        if string[35:42] == "PcaSvc ":
            w[2] = str(int(string[11:34]))
    return w

def smallDump(pid):
    if sapphireCheck():
        popUp("Kangaroo","Confirmed Anti-SS Tool Found")
        return 0
    cmd = "C:/Windows/Temp/strings2.exe -pid " + str(pid) + " -raw -l 5"
    a = str(subprocess.check_output(cmd)).split("\\r\\n")
    b = list(set(a))
    return b

def isShortExe(string):
    alpha = "abcdefghijklmnopqrstuvwxyz1234567890_ ()."
    for char in string:
        if char not in alpha:
            return False
    return (".exe" == string[len(string)-4:].lower())

def isTrace(string):
    return (".exe\\r" == string[len(string)-6:].lower() and "TRACE," in string)

def isValid(string):
    if ".exe!" in string and string[0:2] == "!!":
        return True
    else:
        return False

def getSmallExes(arr,p):
    exes = []
    if p == 0:
        for string in arr:
            if isValid(string):
                exes.append(getName(string))
    elif p == 1:
        for string in arr:
            if isHarddisk(string):
                s2 = string[string.rindex("\\\\")+2:]
                exes.append(s2)
    elif p == 2:
        for string in arr:
            if isTrace(string):
                s2 = string[string.rindex("\\\\")+2:len(string)-2]
                exes.append(s2)
    return exes

def getName(string):
    return string[2:][0:string[2:].index("!")]

def getDate(string):
    return string[2:][string[2:].index("!")+1:][0:string[2:][string[2:].index("!")+1:].index("!")]

def isRecent(exe):
    try:
        ds = getDate(exe)
        cyear = int(ds[0:4])
        cmonth = int(ds[5:7])
        cday = int(ds[8:10])
        a = str(datetime.date.today())
        nyear = int(a[0:4])
        nmonth = int(a[5:7])
        nday = int(a[8:10])
        if nyear==cyear and nmonth==cmonth and abs(nday-cday) < 2:
            return True
        else:
            return False
    except:
        return False

def external2():
    os.system("cls")
    PIDS = getPIDs() 
    if int(PIDS[0]) == 0:
        popUp("Kangaroo","Missing Process!")
        return 0
    DPSARR = smallDump(PIDS[0])
    bigdps = str(DPSARR).lower()
    dps = getSmallExes(DPSARR,0)
    missing = []
    sketches = []
    cheats = []
    new = []
    bads = ['.exe!2018/12/21:18:35:25:_:Confirmed Cheat #1', '.exe!2018/12/22:01:55:17:_:Confirmed Cheat #2', '.exe!2017/11/23:17:49:12:_:Confirmed Cheat #3', '.exe!2018/07/30:21:27:28:_:Confirmed Cheat #4', '.exe!2018/07/24:12:25:08:_:Confirmed Cheat #4', '.exe!2018/07/24:11:25:08:_:Confirmed Cheat #6', '.exe!2018/10/27:18:43:56:_:Confirmed Cheat #7', '.exe!2018/12/23:12:20:12:_:Confirmed Cheat #8', '.exe!2018/12/23:07:20:12:_:Confirmed Cheat #9', '.exe!2105/11/05:13:17:26:_:Confirmed Cheat #10', '.exe!2016/03/26:11:46:09:_:Confirmed Cheat #11', '.exe!1970/01/02:12:24:32:_:Confirmed Cheat #12', '.exe!2096/06/15:14:43:01:_:Confirmed Cheat #13', '.exe!1972/11/25:22:00:32:_:Confirmed Cheat #14', '.exe!2017/12/07:16:54:47:_:Confirmed Cheat #15', '.exe!2075/06/10:00:22:57:_:Confirmed Cheat #16', '.exe!2018/12/02:10:05:56:_:Confirmed Cheat #17', '.exe!2019/05/27:04:31:42:_:Confirmed Cheat #18', '.exe!2019/04/17:21:30:24:_:Confirmed Cheat #19', '.exe!2018/08/06:02:14:23:_:Confirmed Cheat #20', '.exe!2019/02/22:15:29:56:_:Confirmed Cheat #21', '.exe!2018/07/07:08:19:30:_:Confirmed Cheat #22', '.exe!2019/03/19:15:35:31:_:Confirmed Cheat #23', '.exe!2019/03/21:17:39:00:_:Confirmed Cheat #24', '.exe!2019/06/03:03:35:47:_:Confirmed Cheat #25', '.exe!2017/07/21:17:27:54:_:Confirmed Cheat #26', '.exe!2018/12/01:22:19:03:_:Confirmed Cheat #27', '.exe!2073/09/17:20:30:37:_:Confirmed Cheat #28', '.exe!2019/02/04:07:36:49:_:Confirmed Cheat #29', '.exe!2019/04/05:20:07:23:_:Confirmed Cheat #30', '.exe!2019/04/05:20:07:23:_:Confirmed Cheat #32', '.exe!2017/05/09:11:06:24:_:Confirmed Cheat #33', '.exe!2019/06/03:03:35:47:_:Confirmed Cheat #34', '.exe!2071/02/05:13:05:38:_:Confirmed Cheat #35', '.exe!2019/06/29:22:18:29:_:Confirmed Cheat #36', '.exe!2017/11/05:20:20:19:_:Confirmed Cheat #37', '.exe!2018/08/05:06:19:40:_:Confirmed Cheat #38', '.exe!1970/01/01:00:00:00!5c9905!:_:Confirmed Cheat #39', '.exe!1970/01/01:00:00:00!745602!:_:Confirmed Cheat #40', '.exe!1970/01/01:18:12:16!194d6!:_:Confirmed Cheat #41', '.exe!2012/02/14:16:12:40:_:Confirmed Autoclicker #1', '.exe!2008/05/24:11:53:46:_:Confirmed Autoclicker #2', '.exe!2016/06/14:15:35:10:_:Confirmed Autoclicker #3', '.exe!2019/05/22:20:55:54:_:Confirmed Autoclicker #4', '.exe!2008/05/12:01:20:55:_:Confirmed Autoclicker #5', '.exe!2016/09/12:02:07:50:_:Confirmed Autoclicker #6', '.exe!2019/05/25:15:32:34:_:String Cleaner #1', '.exe!2019/05/25:15:32:00:_:String Cleaner #2', '.exe!2019/05/25:15:27:07:_:String Cleaner #3', '.exe!2019/05/25:15:30:08:_:String Cleaner #4', '.exe!2019/05/25:15:31:29:_:String Cleaner #5', '.exe!2018/09/25:23:03:33:_:Smooqy KB Modifier', '.exe!2016/04/18:10:55:45:_:Speed AutoClicker', '.exe!2018/12/30:20:36:45:_:TheFastestMouseClicker', '.exe!2016/04/07:19:35:35:_:FastClicker', '.exe!2010/11/02:22:03:56:_:ClickyGone Window Hider', '.exe!2018/08/28:16:34:26:_:Buzkaa Clicker', '.exe!2017/06/10:11:04:24:_:BySkyCraft Autoclicker', '.exe!2017/11/02:07:46:04:_:Vepe Clicker (Pain Clicker is a skid of this as well)', '.exe!2013/07/20:15:03:24:_:Armax2001 Autoclicker', '.exe!2019/02/09:07:28:06:_:Drip', '.exe!2019/05/11:17:47:20:_:Entropy', '.exe!2017/12/05:19:59:28:_:Demon', '.exe!2019/05/03:20:13:18:_:Matic', '.exe!2018/07/24:12:25:57:_:Apollo Lite', '.exe!2018/07/24:11:25:57:_:Apollo Lite', '.exe!2017/03/21:16:53:34:_:AutoMemer', '.exe!2018/08/22:07:49:38:_:BAIT B1', '.exe!2088/05/02:08:41:52:_:Banked Clicker', '.exe!2017/06/27:02:48:00:_:Beaner Clicker', '.exe!2055/03/08:00:35:40:_:Cr1sPvP Clicker', '.exe!2018/12/09:16:58:13:_:Cucklord Cracked', '.exe!2018/03/17:11:43:49:_:Goon Clicker', '.exe!2015/11/11:11:05:03:_:Lemons Clicker V2', '.exe!2016/08/02:10:49:29:_:Malwarebytes Clicker', '.exe!2012/02/14:16:12:40:_:ManoLucarioDeadMauFodaDe idk wtf this is', '.exe!2016/02/25:00:55:14:_:Microsoft Office Installer Clicker', '.exe!2016/03/26:15:46:09:_:nacl 32 Clicker', '.exe!2017/02/13:00:44:51:_:Notepad Clicker', '.exe!2018/06/14:01:21:45:_:Op AutoClicker', '.exe!2017/06/01:13:26:40:_:Spotify Clicker', '.exe!2017/07/16:01:17:57:_:Tap Client', '.exe!2016/01/24:01:39:00:_:Thoiry Client', '.exe!2013/07/20:17:35:28:_:Unknow Clicker', '.exe!2017/10/08:19:20:26:_:Grape', '.exe!2017/10/09:18:25:54:_:Indigo', '.exe!2017/09/07:02:55:26:_:Meth', '.exe!2018/11/09:01:13:38:_:Ghostbytes', '.exe!2018/10/21:19:34:21:_:Ecstasy', '.exe!2019/05/21:16:37:17:_:Latemod', '.exe!2018/11/03:02:34:55:_:Plow Clicker', '.exe!2018/10/10:19:00:42:_:Tap Client', '.exe!2019/04/15:12:11:37:_:Flex v2 Autoclicker', '.exe!2018/04/11:19:55:52:_:Drip Cracked', '.exe!2018/06/09:06:47:44:_:Universal Client', '.exe!2018/11/07:21:00:33:_:Mithril Ghost Client', '.exe!2018/09/02:13:56:05:_:Mars Autoclicker', '.exe!2018/09/07:10:47:57:_:Mars Autoclicker', '.exe!2019/07/11:12:20:09:_:Glock Clicker (Cracked)', '.exe!2042/04/09:09:23:55:_:Blue Lite', '.exe!2019/06/03:03:35:47:_:Vape Lite', '.exe!2018/11/27:23:46:33:_:Vape Lite (2)', '.exe!2019/06/22:07:36:56:_:Manthe Clicker', '.exe!2019/06/23:03:17:25:_:Manthe Clicker (2)', '.exe!2019/08/19:19:01:21:_:Privileged Memory Hack', '.exe!2018/04/30:22:42:12:_:Air External Autoclicker', '.exe!2099/06/28:14:57:00:_:Dragon Memory Hack', '.exe!2016/07/20:11:52:56:_:Cracked Vape Launcher']
    if not (int(PIDS[2]) == 0):
        PCAARR = smallDump(PIDS[2])
        pca = getSmallExes(PCAARR,2)
        bigpca = str(PCAARR).lower()
        for string in PCAARR:
            if isTrace(string):
                if (string[string.rindex("\\\\")+2:len(string)-2].lower() not in bigdps and "\\users\\" in string.lower() and "appdata" not in string.lower()):
                    long = string[string.lower().rindex("c:\\"):len(string)-2].replace("\\\\","\\")
                    missing.append(long)
                if isSketchy(string[string.rindex("\\\\")+2:len(string)-2]) and "\\users\\" in string.lower():
                    sketches.append(string[string.lower().rindex("c:\\")+2:len(string)-2].replace("\\\\","\\"))
    for bad in bads:
        for exe in DPSARR:
            if isValid(exe):
                if cstring(bad) in exe:
                    try:
                        if getName(exe).lower() in bigpca:
                            cheats.append(getName(exe) + "\t("+ cname(bad) +")")
                    except:
                        cheats.append(getName(exe) + "\t("+ cname(bad) +")")
                if isSketchy(getName(exe)):
                    sketches.append(getName(exe))
                if isRecent(exe) and "delta" not in exe.lower():
                    new.append(getName(exe))
                    
    missing = list(set(missing))
    sketches = list(set(sketches))
    cheats = list(set(cheats))
    new = list(set(new))
    deleted = []
    for long in missing:
        if not os.path.isfile(long):
            deleted.append(long)
            missing.remove(long)

    if len(missing) == 0 and len(sketches) == 0 and len(cheats) == 0 and len(new) == 0:
        popUp("Kangaroo","Nothing found!")
    else:
        msg = "POSSIBLE CHEATS:\n================"
        for exe in cheats:
            msg += "\n [S=4]" + exe
        for exe in deleted:
            msg += "\n [S=3]" + exe + "\t(DELETED)"
        for exe in new:
            msg += "\n [S=2]" + exe + "\t(New)"
        for exe in missing:
            msg += "\n [S=2] " + exe + "\t(Unaccounted for)"
        for exe in sketches:
            msg += "\n [S=1] " + exe + "\t(Weird Name?)"
        popUp("Kangaroo",msg)
    

def selfDestruct():
    f = open("end.bat","w")
    f.write("@echo off\n")
    f.write('taskkill /F /IM '+ str(os.getpid()) +'\n')
    f.write("timeout /t 2 /nobreak > NUL\n")
    f.write("del C:/Windows/Temp/strings2.exe\n")
    f.write("del Kangaroo.exe\n")
    f.write("del end.bat")
    f.close()
    os.system("end.bat")

# Please don't make fun of this function, I'm aware I can just use a URL decoder, but I'm lazy
def cleann(string):
    string = string.replace("%20"," ")
    string = string.replace("%21","%")
    string = string.replace("%23","#")
    string = string.replace("%24","$")
    string = string.replace("%26","&")
    string = string.replace("%27","'")
    string = string.replace("%28","(")
    string = string.replace("%29",")")
    string = string.replace("%2B","+")
    string = string.replace("%2C",",")
    string = string.replace("%2D","-")
    string = string.replace("%2E",".")
    string = string.replace("%3B",";")
    string = string.replace("%3D","=")
    string = string.replace("%40","@")
    string = string.replace("%5B","[")
    string = string.replace("%5D","]")
    string = string.replace("%5E","^")
    string = string.replace("%5F","_")
    string = string.replace("%60","`")
    string = string.replace("%4B","{")
    string = string.replace("%4D","}")
    string = string.replace("%4E","~")
    string = string.replace("%52",",")
    string = string.replace("%25","%")
    return string

def oldClassesQuick(dump):
    classes = []
    mods = []
    combined = []
    both = []
    for string in dump:
        if ".class" in string and "/.minecraft/mods/" in string and "forge" not in string and "batty" not in string.lower():
            classs = string[string.rindex("/")+1:string.index(".class")+6]
            mod = string[string.lower().index("c:"):string.rindex(".jar")+4].replace("%20"," ")
            mod = cleann(mod)
            classes.append(classs)
            mods.append(mod)
            combined.append(mod[mod.rindex("/")+1:]+": "+classs)
    combined = list(set(combined))
    classes = list(set(classes))
    mods = list(set(mods))
    both = [mods,classes,combined]
    return both

def nowClasses(arr):
    big = []
    for mod in arr:
        try:
            f = open(mod,"rb")
            dump1 = str(f.read())
            f.close()
        except:
            dump1 = ""
            fullygone.append(mod)
        length = len(dump1)
        cnum = 0
        small = ""
        while cnum < length-1:
            if str(dump1[cnum:cnum+2]) == str('\\x'):
                cnum += 4
            elif str(dump1[cnum]) not in str('\\\r'):
                small += str(dump1[cnum])
                cnum += 1
            else:
                if len(small) > 3:
                    big.append(small)
                small = ""
                cnum += 1
        big = list(set(big))
    return "".join(big)

def DCC(dump):
    try:
        os.system("cls")
        os.system("color 0b")
        fullygone = []
        a = oldClassesQuick(dump)
        memclasses = a[1]
        mods = a[0]
        modandclass = a[2]
        b = nowClasses(mods)
        notfound = []
        msg = "Nothing found!"
        for clas in memclasses:
            if clas not in b:
                for modc in modandclass:
                    if clas in modc:
                        notfound.append(modc)
        notfound = list(set(notfound))
        if len(notfound) > 0:
            msg = "DELETED CLASSES:\n============\n"
            msg += "\n".join(notfound)
        if len(fullygone) > 0:
            msg += "\n\nDELETED MODS:\n===========\n"
            msg += "\n".join(fullygone)
        popUp("Deleted Class Scan [2/3]",msg)
    except:
        popUp("Deleted Class Scan [2/3]","Error: Unable to determine deleted classes")

def getExeName(string):
    string2 = ""
    for charnum in range(len(string)):
        if string[charnum:charnum+2] == "c:":
            return makeLookNice(string[charnum:])

def shrink(arr):
    arr2 = []
    for string in arr:
        if ".exe" in string.lower() and "sers" in string and "Kangaroo" not in string:
            arr2.append(string.lower())
            arr2 = list(set(arr2))
    return arr2

def echeck(arr):
    arrc = [".exe.part","??\\c:","file:///","file:c:","exe.manifest","exe.config",".partial","zone.identifier"]
    arr2 = []
    for string in arr:
        for string2 in arrc:
            if string2 in string:
                if getExeName(string) != None:
                    arr2.append(getExeName(string))
    arr2 = list(set(arr2))
    return arr2
    
def dumpProcess(procName):
    if sapphireCheck():
        popUp("Kangaroo","Confirmed Anti-SS Tool Found")
        return 0
    file = 'C:/Windows/Temp/' + str(procName) + '.txt'
    dumpcmd = 'for /f "tokens=2" %%a in (\'tasklist^|find /i "'+ str(procName) +'"\') do ( @echo Dumping '+ str(procName) +'.exe - %%a &&C:/Windows/Temp/strings2.exe -pid %%a -raw >>'+ file + ' )'
    b = open('C:/Windows/Temp/dump.bat', 'w')
    b.write('@echo off\n')
    b.write(dumpcmd + '\n')
    b.write('exit\n')
    b.close()
    time.sleep(1)
    p = Popen('C:/Windows/Temp/dump.bat')
    p.wait()
    os.remove('C:/Windows/Temp/dump.bat')
    return file

def read(filename):
    arr = []
    f = open(filename)
    for line in f:
        try:
            line = line[0:len(line)-1]
            if len(line) > 4 and len(line) < 100:
                arr.append(line)
        except:
            pos = 0
    f.close()
    arr = list(set(arr))
    os.remove(filename)
    return arr

def makeLookNice(string):
    string2 = ""
    string2 = string.replace("/","\\")
    string2 = string2.replace("%20"," ")
    string2 = string2.replace(".config","")
    string2 = string2.replace(".manifest","")
    string2 = string2.lower().replace(":zone.identifier","")
    return string2

def moddedDate(file):
    return datetime.datetime.fromtimestamp(os.stat(file).st_mtime)

def timeSinceMod(file):
    try:
        return time.time() - os.stat(file).st_mtime
    except:
        if "/" in string:
            a = "/"
        elif "\\" in string:
            a = "\\"
        return time.time - os.stat(file[file.index("c:"):file.rindex(a)]).st_mtime

def getRecentlyModded(exes):
    recents = []
    for exe in exes:
        try:
            path = getPath(exe)
            if 0 < timeSinceMod(path) < 1800:
                recents.append(path)
        except:
            pass
    recents = list(set(recents))
    return recents

def exesInDir(path):
    c = []
    a = os.listdir(path)
    for b in a:
        if b[len(b)-4:] == ".exe":
            c.append(b)
    return c

def collide(string):
    string2 = ""
    for char in string:
        string2 += chr(ord(char)%5+65)
    return string2

def kangarooGenerics():
    os.system("color 0b")
    os.system("cls")
    x = getStartTime()
    w = getStartTime2()
    t1 = time.time()
    if sapphireCheck():
        popUp("Kangaroo","Confirmed Anti-SS Tool Found")
        return 0
    a1 = dumpProcess('explorer')
    a2 = list(set(read(a1)))
    a3 = shrink(a2)
    a4 = getRecentlyModded(a3)
    arr = echeck(a3)
    c = nonexistant(arr)
    yy = collide("%20".join(a2))
    yyy = "CDCCAAABEACABABBEBACCABEAAABBBAB"
    if yyy not in yy and str(x) in str(w):
        z = True
    else:
        z = False
    
    f = open("results.txt","w")
    f.write("============= Explorer Start Time =================\n")
    if z == True:
        x += "."
    f.write(x + "\n\n")
    
    f.write("============= Sketchy Executables =================\n")
    for L in c:
        f.write("["+dateModded(getPath(L))+"] "+L+"\n")
    f.write("\n")
    f.write("============= Other Executables ===================\n")
    for L in arr:
        f.write("["+dateModded(getPath(L))+"] "+L+"\n")
    f.write("\n")
    f.write("============= Recently Modified Paths =============\n")
    for L in a4:
        if len(exesInDir(L)) > 0:
            f.write(L+"\n")
            for exe in exesInDir(L):
                f.write("   - " + exe + "\n")
    f.write("\n")
    f.close()
    t2 = time.time()
    scantime = str(t2 - t1)
    if len(scantime) > 4:
        scantime = scantime[0:4]
    os.system("notepad.exe results.txt")
    os.remove("results.txt")

def getStartTime():
    a = str(subprocess.check_output("powershell (Get-Date (Get-Process explorer).StartTime)"))
    b = a[6:]
    for charnum in range(len(b)):
        if b[charnum] == "\\":
            return str(b[:charnum])

def getStartTime2():
    a = str(subprocess.check_output("powershell (Get-Date (Get-Process lsass).StartTime)"))
    b = a[6:]
    for charnum in range(len(b)):
        if b[charnum] == "\\":
            return str(b[:charnum])

def dateModded(path):
    try:
        date = str(datetime.fromtimestamp(mktime(time.localtime(max(os.path.getmtime(path), os.path.getctime(path))))))
    except:
        date = "99999999999999999999999999999999999999999999999999999"
    year = date[0:4]
    day = date[8:10]
    month = date[5:7]
    hour = date[11:13]
    minute = date[14:16]
    suffix = " AM"
    if int(hour) > 11:
        if int(hour) != 12:
            prefix = ""
            if int(hour) < 22:
                prefix = "0"
            hour = prefix+str(int(hour)-12)
        suffix = " PM"
    new = month+"/"+day+"/"+year+" "+hour+":"+minute+suffix
    return new

def getPath(file):
    return file[file.lower().index("c:"):file.rindex("\\")]

def nonexistant(arrE):
    nonexistants = []
    existants = []
    for exeE in arrE:
        if not os.path.isfile(str(exeE)):
            nonexistants.append(str(exeE))
    return nonexistants

def pcaName(exe):
    try:
        exe2 = exe[exe.rindex("/")+1:]
        exe2 = exe2[:exe2.index(".exe")] + ".exe"
    except:
        exe2 = "R"
    return exe2

def pcaPID():
    a = str(subprocess.check_output("tasklist /svc /FI \"IMAGENAME eq svchost.exe\"")).split("\\r\\n")
    w = 0
    for string in a:
        if string[35:42] == "PcaSvc ":
            w = str(int(string[11:34]))
    return w

def pcaDump(pid):
    if not pid == 0:
        cmd = "C:/Windows/Temp/strings2.exe -pid " + str(pid) + " -raw -l 5"
        a = str(subprocess.check_output(cmd)).split("\\r\\n")
        b = list(set(a))
    else:
        b = []
    return b

def pcaShrink(arr):
    arr2 = []
    for stringQ in arr:
        string = pcaClean(stringQ)
        if ".exe" in string.lower() and ":/Users/" in string[1:9]:
            arr2.append(string[:string.index(".exe")] + ".exe")
    arr2 = list(set(arr2))
    return arr2

def pcaClean(string):
    string2 = ""
    string2 = string.replace("\\\\","/")
    string2 = string2.replace("\\","/")
    string2 = string2.replace("//","/")
    string2 = string2.replace("%20"," ")
    return string2

def exeScan(exes):
    bads = []
    cStrings = ["keystate","windows.form","hwid=","grand0x",".php?","ru59t8","velocity"]
    for exe in exes:
        score = 0
        arr = []
        try:
            f = open(exe,"rb")
            dump = str(f.read(1000000))
            f.close()
            ahh = dump.lower()
            found = False
            for cS in cStrings:
                if found == False:
                    if cS in ahh:
                        bads.append(exe)
                        found = True
        except:
            pass
    return bads


def PCAScan():
    sketches = []
    deleted = []
    noPF = []
    pf = str(list(os.listdir("C:\\Windows\\Prefetch"))).lower()
    w = pcaDump(pcaPID())
    arr = pcaShrink(w)
    if len(w) < 100:
        popUp("External Scan #3","Missing Process; Nothing bad found.")
        return 0
    for exe in arr:
        if isSketchy(pcaName(exe)):
            sketches.append(exe)
        if pcaName(exe).lower() not in pf:
            noPF.append(exe)
    deleted = nonexistant(arr)
    existing = list(set(arr) - set(deleted))
    strange = exeScan(existing)
    if len(deleted) == 0 and len(sketches) == 0 and len(strange) == 0 and len(noPF) == 0:
        popUp("External Scan #3","Nothing found!")
    else:
        msg = "These results are not always reliable and are meant to be looked into further.\n============================== POSSIBLE CHEATS =============================="
        msg += "\n"
        for exe in noPF:
            msg += "\n [Experimental #1] " + exe
        msg += "\n"
        for exe in strange:
            msg += "\n [Experimental #2] " + exe
        msg += "\n"
        for exe in deleted:
            msg += "\n [Executed/Deleted] " + exe
        msg += "\n"
        for exe in sketches:
            msg += "\n [Weird Name] " + exe
        f = open("results.txt","w")
        f.write(msg)
        f.close()
        os.system("notepad.exe results.txt")
        os.remove("results.txt")

def dumpProcessKGEN(procName):
    file = 'C:/Windows/Temp/' + str(procName) + '.txt'
    dumpcmd = 'for /f "tokens=2" %%a in (\'tasklist^|find /i "'+ str(procName) +'"\') do ( @echo Dumping '+ str(procName) +'.exe - %%a &&C:/Windows/Temp/strings2.exe -pid %%a -raw >>'+ file + ' )'
    b = open('C:/Windows/Temp/dump.bat', 'w')
    b.write('@echo off\n')
    b.write(dumpcmd + '\n')
    b.write('exit\n')
    b.close()
    time.sleep(1)
    p = Popen('C:/Windows/Temp/dump.bat')
    p.wait()
    os.remove('C:/Windows/Temp/dump.bat')
    f = open(file)
    arr = list(set(str(f.read()).split("\n")))
    f.close()
    os.remove(file)
    return arr

def getSmallName(path):
    try:
        return path[path.rindex("/")+1:]
    except:
        return path

def getPathKGEN(file):
    return file[file.lower().index("c:"):file.rindex("/")+1]

def getRecentlyModdedKGEN(exes):
    recents = []
    for exe in exes:
        try:
            path = getPathKGEN(exe.lower())
            T = timeSinceMod(path)
            if 0 < T < 7200:
                recents.append("("+str(int(T/60))+" minutes ago) " + exe)
        except:
            pass
    recents = list(set(recents))
    return recents

def clean(string):
    try:
        start = string.lower().index("c:")
        end = string.lower().index(".exe")
        stringC = string[start:end+4]
        stringC = stringC.replace("\\\\","/").replace("\\","/").replace("//","/").replace("%20"," ")
    except:
        stringC = "Delete_93"
    return stringC

def multiDir(files):
    dupes = []
    dupeNames = []
    names = []
    for file in files:
        curName = getSmallName(file)
        if curName in names:
            dupeNames.append(curName)
        else:
            names.append(curName)
    dupeNames = list(set(dupeNames))
    for name in dupeNames:
        temps = []
        a = False
        b = False
        for path in files:
            if name in path:
                temps.append(path)
        for temp in temps:
            if os.path.isfile(temp):
                a = True
                dummy = temp
            else:
                b = True
                other = temp
        if a and b:
            dupes.append(dummy)
    return dupes

def KGen3():
    os.system("cls")
    ExpExes = shrink(dumpProcessKGEN("explorer"))
    dupes = getRecentlyModdedKGEN(multiDir(ExpExes))
    if len(dupes) > 0:
        popUp("Kangaroo","\t\t\tModified Paths\n" + "="*46 + "\n"+"\n\n".join(dupes))
    else:
        popUp("Kangaroo","Nothing found!")

def yesno(msg):
    MsgBox = tkinter.messagebox.askquestion ("Kangaroo",msg)
    if MsgBox == 'yes':
        return 1
    else:
        return 0

def fun(arg,guimode):
    if guimode == 1:
        return 1
    if arg == 1:
        root.title("WAIT...")
        kangarooGenerics()
        root.title("[Kangaroo SS Tool v5.7] ~ By Heklo")
        b1.config(bg='aquamarine')
    elif arg == 2:
        root.title("WAIT...")
        external2()
        root.title("[Kangaroo SS Tool v5.7] ~ By Heklo")
        b2.config(bg='aquamarine')
    elif arg == 3:
        root.title("WAIT...")
        PCAScan()
        root.title("[Kangaroo SS Tool v5.7] ~ By Heklo")
        b3.config(bg='aquamarine')
    elif arg == 4:
        root.title("WAIT...")
        KGen3()
        root.title("[Kangaroo SS Tool v5.7] ~ By Heklo")
        b4.config(bg='aquamarine')
    elif arg == 5:
        root.title("WAIT...")
        dumpJavaw()
        root.title("[Kangaroo SS Tool v5.7] ~ By Heklo")
        b5.config(bg='aquamarine')


##################### MODE #####################
guitestmode = 0                                #
################################################


if not guitestmode:
    adminCheck()
    recordingCheck()

root = Tk()
root.title("[Kangaroo SS Tool v5.7] ~ By Heklo")
root.config(bg="lavender")
root.geometry("400x185")

label_one = Label(root, text = 'Kangaroo v5.7',font=("Courier",35,"bold"),bg="lavender")
label_one.pack()

b1 = Button(root, width=600, text="External Scan #1 (Kangaroo Generics)", bg='medium aquamarine', command=lambda: fun(1,guitestmode))
b1.pack()
b2 = Button(root, width=600, text="External Scan #2 (Specific Detector)", bg='medium aquamarine', command=lambda: fun(2,guitestmode))
b2.pack()
b3 = Button(root, width=600, text="External Scan #3 (Strange Behavior)", bg='medium aquamarine', command=lambda: fun(3,guitestmode))
b3.pack()
b4 = Button(root, width=600, text="External Scan #4 (Path Spoofing)", bg='medium aquamarine', command=lambda: fun(4,guitestmode))
b4.pack()
b5 = Button(root, width=600, text="Internal Scan (Javaw Check)", bg='medium aquamarine', command=lambda: fun(5,guitestmode))
b5.pack()

if not guitestmode:
    root.protocol("WM_DELETE_WINDOW", selfDestruct)

root.mainloop()



















































# 1000 lines
