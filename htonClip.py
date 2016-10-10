import pyperclip
sel = hou.selectedNodes()
cont = [""]
for nodes in sel:
    cont.append('@'+nodes.name())
    for i in range(int(hou.playbar.playbackRange()[0]), int(hou.playbar.playbackRange()[1])+1):
        wTr = nodes.worldTransformAtTime(hou.frameToTime(i))
        out = str(i)+","+str(round(wTr.extractTranslates()[0]*1000)/1000)+","+str(round(wTr.extractTranslates()[1]*1000)/1000)+","+str(round(wTr.extractTranslates()[2]*1000)/1000)+","+str(round(wTr.extractRotates()[0]*1000)/1000)+","+str(round(wTr.extractRotates()[1]*1000)/1000)+","+str(round(wTr.extractRotates()[2]*1000)/1000)
        cont.append(out)
out = '_'.join(cont)
pyperclip.copy(out)
