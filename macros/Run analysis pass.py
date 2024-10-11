#################################################################################
## GPo 2022, AvsPmod macro 'Run analysis pass.py', last Update 9.10.2024
## Like menu 'Run analysis pass' but in a separate thread. 
## Therefore you can continue working with AvsPmod on another tab (script).
## But it is a bit slower than 'Run analysis pass' from the AvsPmod tools menu. 
#################################################################################

import wx, threading, time, tempfile
import  pyavs, wxp

# init_only > there are functions, e.g. the SceneLog DBSC from StainlessS that runs through its own frame loop
# and then returns the result or writes it to a file. Set it to True, a dialog is then displayed and you can disable it.
init_only = False 

self = avsp.GetWindow()
script = self.currentScript

if init_only:
    ID = wxp.MessageBox("Single pass is enabled 'init_only'. Change it?", 'Analysis pass', wx.YES_NO, self)
    if ID == wx.YES:    
        init_only = False
     
def runpass(progress, txt, filename, workdir, init_only):
    
    if init_only:
        initial_time = time.time()
    avsp.SafeCall(progress.Start)

    AVI = pyavs.AvsSimpleClipBase(txt, filename=filename, workdir=workdir)
    if AVI is None:
        avsp.SafeCall(progress.Close)
        avsp.SafeCall(avsp.MsgBox,'Cannot create AvsSimpleClipBase', 'Analysis pass error')
        return
    if AVI.error_message is not None:
        AVI = None
        avsp.SafeCall(progress.Close)
        avsp.SafeCall(avsp.MsgBox, AVI.error_message, 'Analysis pass error')
        return
       
    if init_only:
        AVI = None
        wx.Bell()
        st = time.strftime("%H:%M:%S", time.gmtime(time.time() - initial_time))
        avsp.SafeCall(progress.Stop)
        avsp.SafeCall(progress.SetLabel, 'Finished at %s' % st, '')
        return
        
    frame_count = AVI.Framecount    
    avsp.SafeCall(progress.SetLabel, 'Running analysis pass', '')
    avsp.SafeCall(progress.SetRange, frame_count)
    previous_frame = -1
    initial_time = previous_time = time.time()
    for frame in range(frame_count):
        AVI.clip.get_frame(frame)
        error = AVI.clip.get_error()
        if error:
            AVI = None
            avsp.SafeCall(progress.Close)
            avsp.SafeCall(avsp.MsgBox, u'\n\n'.join((_('Error requesting frame {number}').format(number=frame), error)), 'Error')
            return
        now = time.time()
        delta = now - previous_time
        elapsed_time = now - initial_time
        if delta >= 0.1: # then elapsed_time > 0, so no check is needed (if elapsed_time else 'INF')
            fps = (frame - previous_frame) / delta
            previous_time = now
            previous_frame = frame
            progress.remaining_time = frame_count * elapsed_time / (frame+1) - elapsed_time
            avsp.SafeCall(progress.Update, frame, _('Average %#.4g fps') % ((frame+1)/ elapsed_time), _('Frame %s/%s (%#.4g fps)') % (frame, frame_count, fps), True)
            if progress.Cancel:
                AVI = None
                avsp.SafeCall(progress.Close)
                return
                
    elapsed_time = time.time() - initial_time
    AVI = None
    wx.Bell()
    avsp.SafeCall(progress.Stop)
    avsp.SafeCall(progress.SetLabel, 'Finished (%s fps average)' % ('%#.4g' % (frame_count / elapsed_time) if elapsed_time else 'INF'), '*** live and let live ***')
    
    
def run(script, init_only):
    filename = workdir = script.filename
    if not filename:
        workdir = tempfile.gettempdir()
    progress = wxp.ProgressDlg(self, 'Analysis pass', 'Process in progress', 'Waiting for clip initialization')
    th = threading.Thread(target=runpass, args=(progress, script.GetText(), filename, workdir, init_only,)) 
    th.daemon = True
    th.start()
   
wx.CallAfter(run, script, init_only)
  
 