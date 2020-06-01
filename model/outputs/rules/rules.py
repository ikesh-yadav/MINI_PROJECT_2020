def findDecision(obj): #obj[0]: gender, obj[1]: friends_time, obj[2]: faculty_time, obj[3]: attendance, obj[4]: attentiveness, obj[5]: co_extra_curricular, obj[6]: study_time, obj[7]: social_time, obj[8]: previous_score, obj[9]: extra_courses, obj[10]: health, obj[11]: sleep_time, obj[12]: library_time
   if obj[4] == 'High':
      if obj[10]>2:
         if obj[8] == '5 to 7':
            if obj[1] == 'sometimes':
               if obj[3] == '75 to 85':
                  if obj[9] == 'often':
                     if obj[2] == 'never':
                        if obj[0] == 'female':
                           return '7 to 9'
                        elif obj[0] == 'male':
                           return '5 to 7'
                        else:
                           return '5 to 7'
                     elif obj[2] == 'sometimes':
                        return '<5'
                     elif obj[2] == 'often':
                        if obj[5] == 'often':
                           return '<5'
                        elif obj[5] == 'sometimes':
                           return '5 to 7'
                        else:
                           return '5 to 7'
                     else:
                        return '<5'
                  elif obj[9] == 'sometimes':
                     if obj[5] == 'often':
                        return '>9'
                     elif obj[5] == 'never':
                        if obj[6] == '1 to 4':
                           return '7 to 9'
                        elif obj[6] == '>4':
                           return '>9'
                        else:
                           return '>9'
                     elif obj[5] == 'sometimes':
                        return '<5'
                     else:
                        return '<5'
                  elif obj[9] == 'never':
                     if obj[5] == 'never':
                        return '<5'
                     elif obj[5] == 'sometimes':
                        return '7 to 9'
                     else:
                        return '7 to 9'
                  else:
                     return '<5'
               elif obj[3] == '>85':
                  if obj[11] == '6 to 8':
                     if obj[7] == '<1':
                        if obj[5] == 'often':
                           if obj[2] == 'never':
                              return '5 to 7'
                           elif obj[2] == 'often':
                              return '7 to 9'
                           elif obj[2] == 'sometimes':
                              return '7 to 9'
                           else:
                              return '7 to 9'
                        elif obj[5] == 'never':
                           return '5 to 7'
                        else:
                           return '5 to 7'
                     elif obj[7] == '>4':
                        if obj[12] == '>4':
                           return '5 to 7'
                        elif obj[12] == '1 to 4':
                           return '7 to 9'
                        else:
                           return '7 to 9'
                     elif obj[7] == '1 to 4':
                        return '5 to 7'
                     else:
                        return '5 to 7'
                  elif obj[11] == '>8':
                     if obj[5] == 'never':
                        return '7 to 9'
                     elif obj[5] == 'sometimes':
                        return '>9'
                     else:
                        return '>9'
                  else:
                     return '7 to 9'
               elif obj[3] == '<75':
                  if obj[5] == 'sometimes':
                     return '7 to 9'
                  elif obj[5] == 'never':
                     if obj[9] == 'never':
                        return '7 to 9'
                     elif obj[9] == 'often':
                        return '5 to 7'
                     else:
                        return '5 to 7'
                  elif obj[5] == 'often':
                     return '>9'
                  else:
                     return '>9'
               else:
                  return '7 to 9'
            elif obj[1] == 'often':
               if obj[11] == '>8':
                  if obj[6] == '>4':
                     if obj[7] == '<1':
                        return '7 to 9'
                     elif obj[7] == '1 to 4':
                        return '>9'
                     elif obj[7] == '>4':
                        return '7 to 9'
                     else:
                        return '7 to 9'
                  elif obj[6] == '1 to 4':
                     if obj[0] == 'female':
                        if obj[2] == 'never':
                           return '5 to 7'
                        elif obj[2] == 'sometimes':
                           return '<5'
                        else:
                           return '<5'
                     elif obj[0] == 'male':
                        return '7 to 9'
                     else:
                        return '7 to 9'
                  elif obj[6] == '<1':
                     if obj[7] == '>4':
                        return '7 to 9'
                     elif obj[7] == '<1':
                        return '7 to 9'
                     elif obj[7] == '1 to 4':
                        return '<5'
                     else:
                        return '<5'
                  else:
                     return '7 to 9'
               elif obj[11] == '6 to 8':
                  if obj[6] == '>4':
                     if obj[2] == 'never':
                        if obj[0] == 'male':
                           return '7 to 9'
                        elif obj[0] == 'female':
                           return '<5'
                        else:
                           return '<5'
                     elif obj[2] == 'sometimes':
                        return '7 to 9'
                     elif obj[2] == 'often':
                        return '5 to 7'
                     else:
                        return '5 to 7'
                  elif obj[6] == '<1':
                     if obj[7] == '>4':
                        return '>9'
                     elif obj[7] == '<1':
                        return '>9'
                     elif obj[7] == '1 to 4':
                        return '7 to 9'
                     else:
                        return '7 to 9'
                  elif obj[6] == '1 to 4':
                     return '7 to 9'
                  else:
                     return '7 to 9'
               elif obj[11] == '<6':
                  if obj[12] == '1 to 4':
                     if obj[2] == 'sometimes':
                        if obj[5] == 'never':
                           if obj[7] == '1 to 4':
                              return '5 to 7'
                           elif obj[7] == '>4':
                              return '7 to 9'
                           else:
                              return '7 to 9'
                        elif obj[5] == 'often':
                           return '5 to 7'
                        else:
                           return '5 to 7'
                     elif obj[2] == 'often':
                        return '7 to 9'
                     else:
                        return '7 to 9'
                  elif obj[12] == '<1':
                     return '5 to 7'
                  elif obj[12] == '>4':
                     return '7 to 9'
                  else:
                     return '7 to 9'
               else:
                  return '5 to 7'
            elif obj[1] == 'never':
               if obj[11] == '6 to 8':
                  if obj[0] == 'male':
                     if obj[7] == '<1':
                        if obj[2] == 'sometimes':
                           if obj[3] == '75 to 85':
                              return '5 to 7'
                           elif obj[3] == '>85':
                              return '<5'
                           else:
                              return '<5'
                        elif obj[2] == 'never':
                           return '5 to 7'
                        elif obj[2] == 'often':
                           return '5 to 7'
                        else:
                           return '5 to 7'
                     elif obj[7] == '>4':
                        if obj[9] == 'often':
                           return '5 to 7'
                        elif obj[9] == 'never':
                           return '7 to 9'
                        elif obj[9] == 'sometimes':
                           return '>9'
                        else:
                           return '>9'
                     elif obj[7] == '1 to 4':
                        return '>9'
                     else:
                        return '>9'
                  elif obj[0] == 'female':
                     return '<5'
                  else:
                     return '<5'
               elif obj[11] == '<6':
                  if obj[2] == 'sometimes':
                     if obj[0] == 'female':
                        if obj[3] == '75 to 85':
                           return '>9'
                        elif obj[3] == '<75':
                           return '5 to 7'
                        else:
                           return '5 to 7'
                     elif obj[0] == 'male':
                        return '7 to 9'
                     else:
                        return '7 to 9'
                  elif obj[2] == 'often':
                     return '7 to 9'
                  elif obj[2] == 'never':
                     if obj[0] == 'male':
                        return '<5'
                     elif obj[0] == 'female':
                        return '7 to 9'
                     else:
                        return '7 to 9'
                  else:
                     return '<5'
               elif obj[11] == '>8':
                  if obj[12] == '>4':
                     if obj[2] == 'never':
                        return '5 to 7'
                     elif obj[2] == 'often':
                        return '<5'
                     else:
                        return '<5'
                  elif obj[12] == '1 to 4':
                     return '>9'
                  elif obj[12] == '<1':
                     return '<5'
                  else:
                     return '<5'
               else:
                  return '<5'
            else:
               return '5 to 7'
         elif obj[8] == '>9':
            if obj[0] == 'male':
               if obj[5] == 'sometimes':
                  if obj[7] == '>4':
                     if obj[9] == 'sometimes':
                        if obj[1] == 'often':
                           if obj[2] == 'often':
                              return '<5'
                           elif obj[2] == 'never':
                              return '7 to 9'
                           else:
                              return '7 to 9'
                        elif obj[1] == 'sometimes':
                           return '7 to 9'
                        else:
                           return '7 to 9'
                     elif obj[9] == 'never':
                        return '>9'
                     elif obj[9] == 'often':
                        return '>9'
                     else:
                        return '>9'
                  elif obj[7] == '1 to 4':
                     if obj[11] == '6 to 8':
                        if obj[2] == 'often':
                           return '7 to 9'
                        elif obj[2] == 'never':
                           return '>9'
                        else:
                           return '>9'
                     elif obj[11] == '<6':
                        return '>9'
                     elif obj[11] == '>8':
                        return '7 to 9'
                     else:
                        return '7 to 9'
                  elif obj[7] == '<1':
                     if obj[12] == '>4':
                        return '7 to 9'
                     elif obj[12] == '1 to 4':
                        if obj[1] == 'never':
                           return '5 to 7'
                        elif obj[1] == 'often':
                           return '7 to 9'
                        else:
                           return '7 to 9'
                     else:
                        return '5 to 7'
                  else:
                     return '7 to 9'
               elif obj[5] == 'never':
                  if obj[7] == '1 to 4':
                     if obj[6] == '>4':
                        if obj[2] == 'never':
                           return '>9'
                        elif obj[2] == 'often':
                           return '<5'
                        elif obj[2] == 'sometimes':
                           return '5 to 7'
                        else:
                           return '5 to 7'
                     elif obj[6] == '<1':
                        return '5 to 7'
                     elif obj[6] == '1 to 4':
                        return '<5'
                     else:
                        return '<5'
                  elif obj[7] == '>4':
                     if obj[6] == '>4':
                        if obj[1] == 'sometimes':
                           return '7 to 9'
                        elif obj[1] == 'never':
                           return '5 to 7'
                        elif obj[1] == 'often':
                           return '5 to 7'
                        else:
                           return '5 to 7'
                     elif obj[6] == '<1':
                        return '<5'
                     elif obj[6] == '1 to 4':
                        return '>9'
                     else:
                        return '>9'
                  elif obj[7] == '<1':
                     if obj[1] == 'never':
                        return '7 to 9'
                     elif obj[1] == 'sometimes':
                        return '5 to 7'
                     else:
                        return '5 to 7'
                  else:
                     return '5 to 7'
               elif obj[5] == 'often':
                  if obj[12] == '1 to 4':
                     if obj[3] == '>85':
                        return '5 to 7'
                     elif obj[3] == '<75':
                        if obj[2] == 'often':
                           return '7 to 9'
                        elif obj[2] == 'never':
                           return '>9'
                        elif obj[2] == 'sometimes':
                           return '5 to 7'
                        else:
                           return '5 to 7'
                     else:
                        return '5 to 7'
                  elif obj[12] == '<1':
                     if obj[6] == '1 to 4':
                        if obj[2] == 'often':
                           if obj[3] == '>85':
                              return '5 to 7'
                           elif obj[3] == '<75':
                              return '7 to 9'
                           else:
                              return '7 to 9'
                        elif obj[2] == 'never':
                           return '7 to 9'
                        else:
                           return '7 to 9'
                     elif obj[6] == '>4':
                        return '5 to 7'
                     else:
                        return '5 to 7'
                  elif obj[12] == '>4':
                     return '7 to 9'
                  else:
                     return '7 to 9'
               else:
                  return '5 to 7'
            elif obj[0] == 'female':
               if obj[7] == '1 to 4':
                  if obj[1] == 'often':
                     if obj[2] == 'never':
                        if obj[3] == '>85':
                           if obj[5] == 'sometimes':
                              return '7 to 9'
                           elif obj[5] == 'often':
                              return '<5'
                           else:
                              return '<5'
                        elif obj[3] == '<75':
                           if obj[5] == 'often':
                              if obj[12] == '1 to 4':
                                 return '>9'
                              elif obj[12] == '>4':
                                 return '7 to 9'
                              else:
                                 return '7 to 9'
                           elif obj[5] == 'never':
                              return '7 to 9'
                           else:
                              return '7 to 9'
                        elif obj[3] == '75 to 85':
                           return '5 to 7'
                        else:
                           return '5 to 7'
                     elif obj[2] == 'often':
                        return '<5'
                     else:
                        return '<5'
                  elif obj[1] == 'sometimes':
                     if obj[3] == '>85':
                        if obj[5] == 'never':
                           return '7 to 9'
                        elif obj[5] == 'often':
                           return '<5'
                        elif obj[5] == 'sometimes':
                           return '<5'
                        else:
                           return '<5'
                     elif obj[3] == '<75':
                        if obj[5] == 'never':
                           return '>9'
                        elif obj[5] == 'often':
                           return '7 to 9'
                        elif obj[5] == 'sometimes':
                           return '7 to 9'
                        else:
                           return '7 to 9'
                     elif obj[3] == '75 to 85':
                        if obj[2] == 'never':
                           return '>9'
                        elif obj[2] == 'sometimes':
                           return '<5'
                        else:
                           return '<5'
                     else:
                        return '<5'
                  elif obj[1] == 'never':
                     if obj[9] == 'sometimes':
                        return '5 to 7'
                     elif obj[9] == 'never':
                        return '<5'
                     else:
                        return '<5'
                  else:
                     return '5 to 7'
               elif obj[7] == '<1':
                  if obj[1] == 'sometimes':
                     if obj[11] == '>8':
                        return '7 to 9'
                     elif obj[11] == '6 to 8':
                        if obj[2] == 'often':
                           return '5 to 7'
                        elif obj[2] == 'never':
                           return '7 to 9'
                        else:
                           return '7 to 9'
                     else:
                        return '5 to 7'
                  elif obj[1] == 'never':
                     if obj[9] == 'never':
                        if obj[5] == 'sometimes':
                           return '<5'
                        elif obj[5] == 'often':
                           return '>9'
                        else:
                           return '>9'
                     elif obj[9] == 'often':
                        return '7 to 9'
                     else:
                        return '7 to 9'
                  elif obj[1] == 'often':
                     return '>9'
                  else:
                     return '>9'
               elif obj[7] == '>4':
                  if obj[11] == '<6':
                     return '5 to 7'
                  elif obj[11] == '>8':
                     if obj[5] == 'often':
                        return '<5'
                     elif obj[5] == 'never':
                        return '5 to 7'
                     else:
                        return '5 to 7'
                  elif obj[11] == '6 to 8':
                     if obj[3] == '75 to 85':
                        return '7 to 9'
                     elif obj[3] == '>85':
                        return '5 to 7'
                     else:
                        return '5 to 7'
                  else:
                     return '5 to 7'
               else:
                  return '5 to 7'
            else:
               return '7 to 9'
         elif obj[8] == '<5':
            if obj[11] == '6 to 8':
               if obj[5] == 'sometimes':
                  if obj[2] == 'often':
                     if obj[6] == '1 to 4':
                        return '5 to 7'
                     elif obj[6] == '<1':
                        if obj[3] == '75 to 85':
                           return '7 to 9'
                        elif obj[3] == '<75':
                           return '5 to 7'
                        else:
                           return '5 to 7'
                     elif obj[6] == '>4':
                        if obj[0] == 'male':
                           return '5 to 7'
                        elif obj[0] == 'female':
                           return '>9'
                        else:
                           return '>9'
                     else:
                        return '5 to 7'
                  elif obj[2] == 'never':
                     if obj[7] == '<1':
                        if obj[1] == 'often':
                           return '>9'
                        elif obj[1] == 'sometimes':
                           return '5 to 7'
                        else:
                           return '5 to 7'
                     elif obj[7] == '>4':
                        return '>9'
                     elif obj[7] == '1 to 4':
                        return '7 to 9'
                     else:
                        return '7 to 9'
                  elif obj[2] == 'sometimes':
                     if obj[1] == 'often':
                        return '>9'
                     elif obj[1] == 'sometimes':
                        if obj[6] == '1 to 4':
                           return '5 to 7'
                        elif obj[6] == '>4':
                           return '>9'
                        else:
                           return '>9'
                     else:
                        return '5 to 7'
                  else:
                     return '>9'
               elif obj[5] == 'never':
                  if obj[9] == 'often':
                     if obj[6] == '<1':
                        return '5 to 7'
                     elif obj[6] == '>4':
                        return '7 to 9'
                     elif obj[6] == '1 to 4':
                        return '7 to 9'
                     else:
                        return '7 to 9'
                  elif obj[9] == 'never':
                     if obj[6] == '>4':
                        return '>9'
                     elif obj[6] == '1 to 4':
                        return '<5'
                     elif obj[6] == '<1':
                        return '<5'
                     else:
                        return '<5'
                  else:
                     return '>9'
               elif obj[5] == 'often':
                  if obj[7] == '1 to 4':
                     if obj[1] == 'never':
                        return '<5'
                     elif obj[1] == 'often':
                        return '<5'
                     elif obj[1] == 'sometimes':
                        return '5 to 7'
                     else:
                        return '5 to 7'
                  elif obj[7] == '<1':
                     return '>9'
                  elif obj[7] == '>4':
                     return '7 to 9'
                  else:
                     return '7 to 9'
               else:
                  return '<5'
            elif obj[11] == '>8':
               if obj[1] == 'sometimes':
                  if obj[0] == 'female':
                     if obj[2] == 'never':
                        if obj[6] == '1 to 4':
                           if obj[9] == 'often':
                              return '>9'
                           elif obj[9] == 'sometimes':
                              return '5 to 7'
                           elif obj[9] == 'never':
                              return '>9'
                           else:
                              return '>9'
                        elif obj[6] == '<1':
                           return '5 to 7'
                        elif obj[6] == '>4':
                           return '<5'
                        else:
                           return '<5'
                     elif obj[2] == 'often':
                        return '>9'
                     elif obj[2] == 'sometimes':
                        return '<5'
                     else:
                        return '<5'
                  elif obj[0] == 'male':
                     if obj[6] == '1 to 4':
                        return '7 to 9'
                     elif obj[6] == '>4':
                        return '>9'
                     else:
                        return '>9'
                  else:
                     return '7 to 9'
               elif obj[1] == 'never':
                  if obj[3] == '<75':
                     if obj[0] == 'female':
                        return '5 to 7'
                     elif obj[0] == 'male':
                        if obj[6] == '1 to 4':
                           return '5 to 7'
                        elif obj[6] == '>4':
                           return '>9'
                        else:
                           return '>9'
                     else:
                        return '5 to 7'
                  elif obj[3] == '75 to 85':
                     return '>9'
                  else:
                     return '>9'
               elif obj[1] == 'often':
                  if obj[5] == 'often':
                     return '>9'
                  elif obj[5] == 'sometimes':
                     return '7 to 9'
                  elif obj[5] == 'never':
                     return '>9'
                  else:
                     return '>9'
               else:
                  return '>9'
            elif obj[11] == '<6':
               if obj[2] == 'sometimes':
                  if obj[9] == 'often':
                     if obj[0] == 'female':
                        if obj[6] == '1 to 4':
                           return '7 to 9'
                        elif obj[6] == '<1':
                           return '5 to 7'
                        elif obj[6] == '>4':
                           return '7 to 9'
                        else:
                           return '7 to 9'
                     elif obj[0] == 'male':
                        return '5 to 7'
                     else:
                        return '5 to 7'
                  elif obj[9] == 'never':
                     if obj[7] == '>4':
                        if obj[12] == '<1':
                           return '>9'
                        elif obj[12] == '1 to 4':
                           return '<5'
                        elif obj[12] == '>4':
                           return '>9'
                        else:
                           return '>9'
                     elif obj[7] == '<1':
                        return '7 to 9'
                     else:
                        return '7 to 9'
                  elif obj[9] == 'sometimes':
                     if obj[0] == 'male':
                        return '<5'
                     elif obj[0] == 'female':
                        return '5 to 7'
                     else:
                        return '5 to 7'
                  else:
                     return '<5'
               elif obj[2] == 'never':
                  if obj[0] == 'female':
                     if obj[1] == 'often':
                        return '5 to 7'
                     elif obj[1] == 'never':
                        return '<5'
                     elif obj[1] == 'sometimes':
                        return '<5'
                     else:
                        return '<5'
                  elif obj[0] == 'male':
                     return '5 to 7'
                  else:
                     return '5 to 7'
               elif obj[2] == 'often':
                  if obj[3] == '>85':
                     return '7 to 9'
                  elif obj[3] == '<75':
                     return '5 to 7'
                  else:
                     return '5 to 7'
               else:
                  return '7 to 9'
            else:
               return '5 to 7'
         elif obj[8] == '7 to 9':
            if obj[7] == '1 to 4':
               if obj[11] == '6 to 8':
                  if obj[5] == 'often':
                     if obj[9] == 'sometimes':
                        if obj[0] == 'male':
                           if obj[1] == 'never':
                              return '5 to 7'
                           elif obj[1] == 'often':
                              return '5 to 7'
                           elif obj[1] == 'sometimes':
                              return '7 to 9'
                           else:
                              return '7 to 9'
                        elif obj[0] == 'female':
                           return '7 to 9'
                        else:
                           return '7 to 9'
                     elif obj[9] == 'never':
                        return '<5'
                     else:
                        return '<5'
                  elif obj[5] == 'sometimes':
                     if obj[0] == 'male':
                        return '>9'
                     elif obj[0] == 'female':
                        return '7 to 9'
                     else:
                        return '7 to 9'
                  elif obj[5] == 'never':
                     return '7 to 9'
                  else:
                     return '7 to 9'
               elif obj[11] == '>8':
                  if obj[0] == 'female':
                     if obj[9] == 'sometimes':
                        return '5 to 7'
                     elif obj[9] == 'never':
                        return '7 to 9'
                     elif obj[9] == 'often':
                        return '7 to 9'
                     else:
                        return '7 to 9'
                  elif obj[0] == 'male':
                     if obj[1] == 'often':
                        return '>9'
                     elif obj[1] == 'never':
                        return '<5'
                     else:
                        return '<5'
                  else:
                     return '>9'
               elif obj[11] == '<6':
                  if obj[1] == 'often':
                     if obj[9] == 'sometimes':
                        return '5 to 7'
                     elif obj[9] == 'often':
                        return '<5'
                     else:
                        return '<5'
                  elif obj[1] == 'sometimes':
                     return '5 to 7'
                  elif obj[1] == 'never':
                     return '<5'
                  else:
                     return '<5'
               else:
                  return '5 to 7'
            elif obj[7] == '<1':
               if obj[0] == 'female':
                  if obj[12] == '1 to 4':
                     if obj[5] == 'never':
                        if obj[11] == '<6':
                           return '>9'
                        elif obj[11] == '6 to 8':
                           if obj[1] == 'never':
                              return '5 to 7'
                           elif obj[1] == 'sometimes':
                              return '<5'
                           else:
                              return '<5'
                        elif obj[11] == '>8':
                           return '>9'
                        else:
                           return '>9'
                     elif obj[5] == 'sometimes':
                        return '5 to 7'
                     elif obj[5] == 'often':
                        return '5 to 7'
                     else:
                        return '5 to 7'
                  elif obj[12] == '>4':
                     return '5 to 7'
                  elif obj[12] == '<1':
                     return '>9'
                  else:
                     return '>9'
               elif obj[0] == 'male':
                  if obj[9] == 'sometimes':
                     if obj[2] == 'sometimes':
                        return '5 to 7'
                     elif obj[2] == 'often':
                        return '>9'
                     else:
                        return '>9'
                  elif obj[9] == 'often':
                     if obj[11] == '>8':
                        return '5 to 7'
                     elif obj[11] == '<6':
                        return '7 to 9'
                     elif obj[11] == '6 to 8':
                        return '>9'
                     else:
                        return '>9'
                  elif obj[9] == 'never':
                     return '7 to 9'
                  else:
                     return '7 to 9'
               else:
                  return '5 to 7'
            elif obj[7] == '>4':
               if obj[0] == 'female':
                  if obj[6] == '>4':
                     if obj[5] == 'never':
                        if obj[12] == '<1':
                           return '>9'
                        elif obj[12] == '1 to 4':
                           return '5 to 7'
                        else:
                           return '5 to 7'
                     elif obj[5] == 'often':
                        return '<5'
                     else:
                        return '<5'
                  elif obj[6] == '1 to 4':
                     if obj[11] == '>8':
                        return '<5'
                     elif obj[11] == '6 to 8':
                        return '<5'
                     elif obj[11] == '<6':
                        return '>9'
                     else:
                        return '>9'
                  elif obj[6] == '<1':
                     return '7 to 9'
                  else:
                     return '7 to 9'
               elif obj[0] == 'male':
                  if obj[5] == 'never':
                     return '7 to 9'
                  elif obj[5] == 'sometimes':
                     if obj[1] == 'never':
                        return '>9'
                     elif obj[1] == 'sometimes':
                        return '7 to 9'
                     else:
                        return '7 to 9'
                  elif obj[5] == 'often':
                     return '>9'
                  else:
                     return '>9'
               else:
                  return '7 to 9'
            else:
               return '7 to 9'
         else:
            return '5 to 7'
      elif obj[10]<=2:
         if obj[8] == '<5':
            if obj[1] == 'often':
               return '5 to 7'
            elif obj[1] == 'never':
               if obj[3] == '75 to 85':
                  return '7 to 9'
               elif obj[3] == '>85':
                  return '>9'
               else:
                  return '>9'
            elif obj[1] == 'sometimes':
               return '7 to 9'
            else:
               return '7 to 9'
         elif obj[8] == '5 to 7':
            if obj[1] == 'sometimes':
               return '<5'
            elif obj[1] == 'often':
               return '5 to 7'
            elif obj[1] == 'never':
               return '5 to 7'
            else:
               return '5 to 7'
         elif obj[8] == '7 to 9':
            if obj[5] == 'sometimes':
               if obj[6] == '<1':
                  return '7 to 9'
               elif obj[6] == '>4':
                  return '<5'
               else:
                  return '<5'
            elif obj[5] == 'never':
               return '5 to 7'
            else:
               return '5 to 7'
         elif obj[8] == '>9':
            if obj[1] == 'never':
               return '5 to 7'
            elif obj[1] == 'often':
               return '7 to 9'
            else:
               return '7 to 9'
         else:
            return '5 to 7'
      else:
         return '5 to 7'
   elif obj[4] == 'Low':
      if obj[10]>2:
         if obj[8] == '5 to 7':
            if obj[12] == '1 to 4':
               if obj[11] == '6 to 8':
                  if obj[6] == '1 to 4':
                     if obj[7] == '1 to 4':
                        if obj[2] == 'often':
                           return '5 to 7'
                        elif obj[2] == 'sometimes':
                           return '>9'
                        else:
                           return '>9'
                     elif obj[7] == '>4':
                        if obj[5] == 'often':
                           return '>9'
                        elif obj[5] == 'never':
                           return '5 to 7'
                        elif obj[5] == 'sometimes':
                           return '<5'
                        else:
                           return '<5'
                     elif obj[7] == '<1':
                        return '<5'
                     else:
                        return '<5'
                  elif obj[6] == '<1':
                     if obj[0] == 'female':
                        if obj[5] == 'sometimes':
                           return '>9'
                        elif obj[5] == 'never':
                           return '<5'
                        elif obj[5] == 'often':
                           return '<5'
                        else:
                           return '<5'
                     elif obj[0] == 'male':
                        if obj[2] == 'never':
                           return '7 to 9'
                        elif obj[2] == 'often':
                           return '>9'
                        else:
                           return '>9'
                     else:
                        return '7 to 9'
                  elif obj[6] == '>4':
                     if obj[0] == 'female':
                        if obj[7] == '<1':
                           return '7 to 9'
                        elif obj[7] == '>4':
                           return '5 to 7'
                        else:
                           return '5 to 7'
                     elif obj[0] == 'male':
                        return '<5'
                     else:
                        return '<5'
                  else:
                     return '7 to 9'
               elif obj[11] == '>8':
                  if obj[2] == 'often':
                     if obj[0] == 'female':
                        if obj[5] == 'sometimes':
                           return '7 to 9'
                        elif obj[5] == 'never':
                           return '>9'
                        else:
                           return '>9'
                     elif obj[0] == 'male':
                        return '<5'
                     else:
                        return '<5'
                  elif obj[2] == 'sometimes':
                     return '5 to 7'
                  elif obj[2] == 'never':
                     if obj[0] == 'female':
                        return '>9'
                     elif obj[0] == 'male':
                        return '5 to 7'
                     else:
                        return '5 to 7'
                  else:
                     return '>9'
               elif obj[11] == '<6':
                  if obj[2] == 'never':
                     if obj[6] == '1 to 4':
                        if obj[5] == 'sometimes':
                           return '5 to 7'
                        elif obj[5] == 'never':
                           return '5 to 7'
                        elif obj[5] == 'often':
                           return '<5'
                        else:
                           return '<5'
                     elif obj[6] == '<1':
                        return '<5'
                     else:
                        return '<5'
                  elif obj[2] == 'sometimes':
                     if obj[5] == 'sometimes':
                        return '5 to 7'
                     elif obj[5] == 'often':
                        return '7 to 9'
                     else:
                        return '7 to 9'
                  elif obj[2] == 'often':
                     return '7 to 9'
                  else:
                     return '7 to 9'
               else:
                  return '5 to 7'
            elif obj[12] == '<1':
               if obj[1] == 'never':
                  if obj[0] == 'male':
                     if obj[2] == 'never':
                        if obj[7] == '1 to 4':
                           if obj[5] == 'never':
                              return '<5'
                           elif obj[5] == 'sometimes':
                              if obj[3] == '>85':
                                 return '<5'
                              elif obj[3] == '<75':
                                 return '7 to 9'
                              else:
                                 return '7 to 9'
                           else:
                              return '<5'
                        elif obj[7] == '>4':
                           return '5 to 7'
                        else:
                           return '5 to 7'
                     elif obj[2] == 'often':
                        if obj[3] == '<75':
                           return '>9'
                        elif obj[3] == '>85':
                           return '<5'
                        else:
                           return '<5'
                     else:
                        return '>9'
                  elif obj[0] == 'female':
                     return '>9'
                  else:
                     return '>9'
               elif obj[1] == 'often':
                  if obj[6] == '>4':
                     if obj[3] == '>85':
                        return '5 to 7'
                     elif obj[3] == '<75':
                        return '<5'
                     else:
                        return '<5'
                  elif obj[6] == '1 to 4':
                     return '7 to 9'
                  elif obj[6] == '<1':
                     return '<5'
                  else:
                     return '<5'
               elif obj[1] == 'sometimes':
                  if obj[0] == 'male':
                     if obj[6] == '1 to 4':
                        return '5 to 7'
                     elif obj[6] == '>4':
                        return '7 to 9'
                     else:
                        return '7 to 9'
                  elif obj[0] == 'female':
                     if obj[11] == '>8':
                        return '>9'
                     elif obj[11] == '<6':
                        return '7 to 9'
                     else:
                        return '7 to 9'
                  else:
                     return '>9'
               else:
                  return '5 to 7'
            elif obj[12] == '>4':
               if obj[6] == '>4':
                  if obj[0] == 'male':
                     if obj[2] == 'never':
                        return '>9'
                     elif obj[2] == 'often':
                        return '>9'
                     elif obj[2] == 'sometimes':
                        return '5 to 7'
                     else:
                        return '5 to 7'
                  elif obj[0] == 'female':
                     if obj[2] == 'sometimes':
                        if obj[9] == 'often':
                           return '7 to 9'
                        elif obj[9] == 'never':
                           return '7 to 9'
                        elif obj[9] == 'sometimes':
                           return '>9'
                        else:
                           return '>9'
                     elif obj[2] == 'never':
                        return '<5'
                     else:
                        return '<5'
                  else:
                     return '7 to 9'
               elif obj[6] == '<1':
                  if obj[3] == '<75':
                     if obj[1] == 'often':
                        return '5 to 7'
                     elif obj[1] == 'never':
                        return '5 to 7'
                     elif obj[1] == 'sometimes':
                        return '7 to 9'
                     else:
                        return '7 to 9'
                  elif obj[3] == '>85':
                     return '7 to 9'
                  elif obj[3] == '75 to 85':
                     return '7 to 9'
                  else:
                     return '7 to 9'
               elif obj[6] == '1 to 4':
                  if obj[0] == 'male':
                     return '>9'
                  elif obj[0] == 'female':
                     if obj[2] == 'never':
                        return '5 to 7'
                     elif obj[2] == 'sometimes':
                        return '7 to 9'
                     else:
                        return '7 to 9'
                  else:
                     return '5 to 7'
               else:
                  return '>9'
            else:
               return '7 to 9'
         elif obj[8] == '<5':
            if obj[12] == '1 to 4':
               if obj[6] == '>4':
                  if obj[3] == '<75':
                     if obj[2] == 'often':
                        if obj[11] == '<6':
                           return '>9'
                        elif obj[11] == '6 to 8':
                           if obj[0] == 'male':
                              if obj[1] == 'never':
                                 return '7 to 9'
                              elif obj[1] == 'sometimes':
                                 return '>9'
                              else:
                                 return '>9'
                           elif obj[0] == 'female':
                              return '>9'
                           else:
                              return '>9'
                        elif obj[11] == '>8':
                           return '5 to 7'
                        else:
                           return '5 to 7'
                     elif obj[2] == 'sometimes':
                        return '>9'
                     elif obj[2] == 'never':
                        return '<5'
                     else:
                        return '<5'
                  elif obj[3] == '>85':
                     if obj[2] == 'never':
                        return '7 to 9'
                     elif obj[2] == 'often':
                        if obj[1] == 'never':
                           return '>9'
                        elif obj[1] == 'sometimes':
                           return '7 to 9'
                        else:
                           return '7 to 9'
                     elif obj[2] == 'sometimes':
                        return '>9'
                     else:
                        return '>9'
                  elif obj[3] == '75 to 85':
                     if obj[5] == 'often':
                        return '7 to 9'
                     elif obj[5] == 'sometimes':
                        return '5 to 7'
                     elif obj[5] == 'never':
                        return '<5'
                     else:
                        return '<5'
                  else:
                     return '7 to 9'
               elif obj[6] == '1 to 4':
                  if obj[7] == '<1':
                     if obj[5] == 'often':
                        if obj[1] == 'often':
                           if obj[0] == 'male':
                              if obj[11] == '<6':
                                 return '5 to 7'
                              elif obj[11] == '6 to 8':
                                 return '7 to 9'
                              else:
                                 return '7 to 9'
                           elif obj[0] == 'female':
                              return '5 to 7'
                           else:
                              return '5 to 7'
                        elif obj[1] == 'sometimes':
                           return '5 to 7'
                        elif obj[1] == 'never':
                           return '7 to 9'
                        else:
                           return '7 to 9'
                     elif obj[5] == 'sometimes':
                        return '>9'
                     elif obj[5] == 'never':
                        return '>9'
                     else:
                        return '>9'
                  elif obj[7] == '1 to 4':
                     if obj[1] == 'never':
                        return '5 to 7'
                     elif obj[1] == 'often':
                        return '7 to 9'
                     elif obj[1] == 'sometimes':
                        return '5 to 7'
                     else:
                        return '5 to 7'
                  elif obj[7] == '>4':
                     return '7 to 9'
                  else:
                     return '7 to 9'
               elif obj[6] == '<1':
                  if obj[1] == 'often':
                     return '7 to 9'
                  elif obj[1] == 'sometimes':
                     return '>9'
                  elif obj[1] == 'never':
                     if obj[0] == 'male':
                        return '>9'
                     elif obj[0] == 'female':
                        return '7 to 9'
                     else:
                        return '7 to 9'
                  else:
                     return '7 to 9'
               else:
                  return '7 to 9'
            elif obj[12] == '>4':
               if obj[11] == '6 to 8':
                  if obj[1] == 'never':
                     if obj[0] == 'female':
                        return '5 to 7'
                     elif obj[0] == 'male':
                        if obj[2] == 'often':
                           return '5 to 7'
                        elif obj[2] == 'sometimes':
                           return '5 to 7'
                        elif obj[2] == 'never':
                           return '>9'
                        else:
                           return '>9'
                     else:
                        return '5 to 7'
                  elif obj[1] == 'often':
                     return '5 to 7'
                  elif obj[1] == 'sometimes':
                     return '>9'
                  else:
                     return '>9'
               elif obj[11] == '<6':
                  if obj[3] == '75 to 85':
                     return '5 to 7'
                  elif obj[3] == '<75':
                     return '7 to 9'
                  else:
                     return '7 to 9'
               else:
                  return '5 to 7'
            elif obj[12] == '<1':
               if obj[2] == 'often':
                  if obj[9] == 'sometimes':
                     if obj[1] == 'never':
                        return '7 to 9'
                     elif obj[1] == 'sometimes':
                        if obj[5] == 'often':
                           return '7 to 9'
                        elif obj[5] == 'sometimes':
                           return '<5'
                        else:
                           return '<5'
                     else:
                        return '<5'
                  elif obj[9] == 'often':
                     return '5 to 7'
                  elif obj[9] == 'never':
                     return '5 to 7'
                  else:
                     return '5 to 7'
               elif obj[2] == 'sometimes':
                  if obj[0] == 'female':
                     if obj[1] == 'never':
                        return '7 to 9'
                     elif obj[1] == 'sometimes':
                        return '<5'
                     else:
                        return '<5'
                  elif obj[0] == 'male':
                     return '>9'
                  else:
                     return '>9'
               elif obj[2] == 'never':
                  return '>9'
               else:
                  return '>9'
            else:
               return '7 to 9'
         elif obj[8] == '>9':
            if obj[5] == 'sometimes':
               if obj[9] == 'sometimes':
                  if obj[7] == '>4':
                     if obj[2] == 'sometimes':
                        if obj[1] == 'often':
                           if obj[0] == 'male':
                              if obj[3] == '>85':
                                 if obj[6] == '>4':
                                    if obj[11] == '<6':
                                       if obj[12] == '1 to 4':
                                          return '<5'
                                       else:
                                          return '<5'
                                    else:
                                       return '<5'
                                 else:
                                    return '<5'
                              else:
                                 return '<5'
                           else:
                              return '<5'
                        elif obj[1] == 'never':
                           return '5 to 7'
                        else:
                           return '5 to 7'
                     elif obj[2] == 'often':
                        return '5 to 7'
                     elif obj[2] == 'never':
                        return '<5'
                     else:
                        return '<5'
                  elif obj[7] == '1 to 4':
                     if obj[0] == 'male':
                        return '7 to 9'
                     elif obj[0] == 'female':
                        return '5 to 7'
                     else:
                        return '5 to 7'
                  elif obj[7] == '<1':
                     if obj[2] == 'often':
                        if obj[0] == 'male':
                           return '5 to 7'
                        elif obj[0] == 'female':
                           return '<5'
                        else:
                           return '<5'
                     elif obj[2] == 'never':
                        return '<5'
                     elif obj[2] == 'sometimes':
                        return '<5'
                     else:
                        return '<5'
                  else:
                     return '<5'
               elif obj[9] == 'never':
                  if obj[2] == 'sometimes':
                     if obj[7] == '1 to 4':
                        return '5 to 7'
                     elif obj[7] == '>4':
                        if obj[1] == 'often':
                           return '5 to 7'
                        elif obj[1] == 'sometimes':
                           return '7 to 9'
                        else:
                           return '7 to 9'
                     elif obj[7] == '<1':
                        return '5 to 7'
                     else:
                        return '5 to 7'
                  elif obj[2] == 'never':
                     if obj[0] == 'female':
                        if obj[6] == '<1':
                           return '<5'
                        elif obj[6] == '1 to 4':
                           return '7 to 9'
                        else:
                           return '7 to 9'
                     elif obj[0] == 'male':
                        if obj[1] == 'never':
                           return '5 to 7'
                        elif obj[1] == 'sometimes':
                           return '7 to 9'
                        else:
                           return '7 to 9'
                     else:
                        return '5 to 7'
                  elif obj[2] == 'often':
                     return '5 to 7'
                  else:
                     return '5 to 7'
               elif obj[9] == 'often':
                  if obj[6] == '1 to 4':
                     return '7 to 9'
                  elif obj[6] == '>4':
                     if obj[0] == 'female':
                        return '>9'
                     elif obj[0] == 'male':
                        return '7 to 9'
                     else:
                        return '7 to 9'
                  elif obj[6] == '<1':
                     if obj[0] == 'male':
                        return '>9'
                     elif obj[0] == 'female':
                        return '<5'
                     else:
                        return '<5'
                  else:
                     return '<5'
               else:
                  return '7 to 9'
            elif obj[5] == 'often':
               if obj[0] == 'male':
                  if obj[1] == 'never':
                     if obj[12] == '<1':
                        return '7 to 9'
                     elif obj[12] == '1 to 4':
                        return '>9'
                     else:
                        return '>9'
                  elif obj[1] == 'sometimes':
                     if obj[3] == '75 to 85':
                        return '5 to 7'
                     elif obj[3] == '>85':
                        return '7 to 9'
                     elif obj[3] == '<75':
                        return '5 to 7'
                     else:
                        return '5 to 7'
                  elif obj[1] == 'often':
                     if obj[2] == 'often':
                        return '5 to 7'
                     elif obj[2] == 'never':
                        return '7 to 9'
                     elif obj[2] == 'sometimes':
                        return '5 to 7'
                     else:
                        return '5 to 7'
                  else:
                     return '5 to 7'
               elif obj[0] == 'female':
                  if obj[11] == '6 to 8':
                     if obj[1] == 'sometimes':
                        if obj[7] == '1 to 4':
                           return '>9'
                        elif obj[7] == '<1':
                           if obj[2] == 'never':
                              return '>9'
                           elif obj[2] == 'sometimes':
                              return '<5'
                           else:
                              return '<5'
                        elif obj[7] == '>4':
                           return '>9'
                        else:
                           return '>9'
                     elif obj[1] == 'often':
                        return '<5'
                     else:
                        return '<5'
                  elif obj[11] == '<6':
                     return '>9'
                  elif obj[11] == '>8':
                     return '5 to 7'
                  else:
                     return '5 to 7'
               else:
                  return '>9'
            elif obj[5] == 'never':
               if obj[1] == 'never':
                  if obj[9] == 'never':
                     return '5 to 7'
                  elif obj[9] == 'sometimes':
                     if obj[3] == '<75':
                        return '<5'
                     elif obj[3] == '75 to 85':
                        return '>9'
                     else:
                        return '>9'
                  elif obj[9] == 'often':
                     if obj[0] == 'male':
                        return '5 to 7'
                     elif obj[0] == 'female':
                        return '>9'
                     else:
                        return '>9'
                  else:
                     return '5 to 7'
               elif obj[1] == 'sometimes':
                  if obj[0] == 'male':
                     if obj[11] == '6 to 8':
                        return '5 to 7'
                     elif obj[11] == '>8':
                        return '5 to 7'
                     elif obj[11] == '<6':
                        return '>9'
                     else:
                        return '>9'
                  elif obj[0] == 'female':
                     if obj[2] == 'often':
                        return '>9'
                     elif obj[2] == 'sometimes':
                        return '<5'
                     else:
                        return '<5'
                  else:
                     return '<5'
               elif obj[1] == 'often':
                  if obj[7] == '<1':
                     return '>9'
                  elif obj[7] == '1 to 4':
                     return '>9'
                  elif obj[7] == '>4':
                     return '<5'
                  else:
                     return '<5'
               else:
                  return '>9'
            else:
               return '5 to 7'
         elif obj[8] == '7 to 9':
            if obj[12] == '1 to 4':
               if obj[9] == 'sometimes':
                  if obj[3] == '75 to 85':
                     if obj[1] == 'never':
                        if obj[5] == 'sometimes':
                           return '<5'
                        elif obj[5] == 'often':
                           return '7 to 9'
                        else:
                           return '7 to 9'
                     elif obj[1] == 'sometimes':
                        if obj[6] == '>4':
                           return '<5'
                        elif obj[6] == '<1':
                           return '5 to 7'
                        else:
                           return '5 to 7'
                     elif obj[1] == 'often':
                        return '>9'
                     else:
                        return '>9'
                  elif obj[3] == '>85':
                     if obj[1] == 'often':
                        return '>9'
                     elif obj[1] == 'sometimes':
                        if obj[6] == '<1':
                           return '7 to 9'
                        elif obj[6] == '1 to 4':
                           return '>9'
                        elif obj[6] == '>4':
                           return '5 to 7'
                        else:
                           return '5 to 7'
                     elif obj[1] == 'never':
                        return '7 to 9'
                     else:
                        return '7 to 9'
                  elif obj[3] == '<75':
                     if obj[7] == '<1':
                        if obj[1] == 'never':
                           if obj[0] == 'male':
                              return '5 to 7'
                           elif obj[0] == 'female':
                              return '>9'
                           else:
                              return '>9'
                        elif obj[1] == 'often':
                           if obj[0] == 'male':
                              return '7 to 9'
                           elif obj[0] == 'female':
                              return '5 to 7'
                           else:
                              return '5 to 7'
                        elif obj[1] == 'sometimes':
                           return '7 to 9'
                        else:
                           return '7 to 9'
                     elif obj[7] == '1 to 4':
                        return '<5'
                     else:
                        return '<5'
                  else:
                     return '5 to 7'
               elif obj[9] == 'often':
                  if obj[11] == '6 to 8':
                     return '5 to 7'
                  elif obj[11] == '>8':
                     if obj[5] == 'never':
                        return '7 to 9'
                     elif obj[5] == 'often':
                        return '5 to 7'
                     elif obj[5] == 'sometimes':
                        return '7 to 9'
                     else:
                        return '7 to 9'
                  elif obj[11] == '<6':
                     return '<5'
                  else:
                     return '<5'
               elif obj[9] == 'never':
                  if obj[3] == '<75':
                     if obj[6] == '<1':
                        return '>9'
                     elif obj[6] == '1 to 4':
                        return '<5'
                     elif obj[6] == '>4':
                        return '>9'
                     else:
                        return '>9'
                  elif obj[3] == '75 to 85':
                     return '7 to 9'
                  elif obj[3] == '>85':
                     return '<5'
                  else:
                     return '<5'
               else:
                  return '>9'
            elif obj[12] == '<1':
               if obj[1] == 'never':
                  if obj[5] == 'never':
                     return '>9'
                  elif obj[5] == 'sometimes':
                     if obj[0] == 'female':
                        if obj[7] == '1 to 4':
                           return '>9'
                        elif obj[7] == '>4':
                           return '7 to 9'
                        else:
                           return '7 to 9'
                     elif obj[0] == 'male':
                        return '7 to 9'
                     else:
                        return '7 to 9'
                  elif obj[5] == 'often':
                     if obj[2] == 'often':
                        return '7 to 9'
                     elif obj[2] == 'sometimes':
                        return '5 to 7'
                     else:
                        return '5 to 7'
                  else:
                     return '5 to 7'
               elif obj[1] == 'often':
                  if obj[7] == '<1':
                     return '5 to 7'
                  elif obj[7] == '1 to 4':
                     return '>9'
                  elif obj[7] == '>4':
                     return '5 to 7'
                  else:
                     return '5 to 7'
               elif obj[1] == 'sometimes':
                  if obj[2] == 'never':
                     return '7 to 9'
                  elif obj[2] == 'often':
                     return '>9'
                  elif obj[2] == 'sometimes':
                     return '7 to 9'
                  else:
                     return '7 to 9'
               else:
                  return '7 to 9'
            elif obj[12] == '>4':
               if obj[6] == '<1':
                  if obj[1] == 'never':
                     if obj[3] == '<75':
                        return '7 to 9'
                     elif obj[3] == '>85':
                        return '5 to 7'
                     elif obj[3] == '75 to 85':
                        return '5 to 7'
                     else:
                        return '5 to 7'
                  elif obj[1] == 'often':
                     if obj[11] == '<6':
                        return '5 to 7'
                     elif obj[11] == '>8':
                        return '<5'
                     elif obj[11] == '6 to 8':
                        return '>9'
                     else:
                        return '>9'
                  elif obj[1] == 'sometimes':
                     if obj[0] == 'male':
                        return '5 to 7'
                     elif obj[0] == 'female':
                        return '>9'
                     else:
                        return '>9'
                  else:
                     return '5 to 7'
               elif obj[6] == '>4':
                  if obj[0] == 'male':
                     return '>9'
                  elif obj[0] == 'female':
                     return '5 to 7'
                  else:
                     return '5 to 7'
               elif obj[6] == '1 to 4':
                  if obj[1] == 'never':
                     return '<5'
                  elif obj[1] == 'often':
                     return '5 to 7'
                  else:
                     return '5 to 7'
               else:
                  return '<5'
            else:
               return '5 to 7'
         else:
            return '>9'
      elif obj[10]<=2:
         if obj[6] == '1 to 4':
            if obj[1] == 'never':
               if obj[9] == 'sometimes':
                  if obj[5] == 'often':
                     return '5 to 7'
                  elif obj[5] == 'sometimes':
                     return '>9'
                  elif obj[5] == 'never':
                     return '5 to 7'
                  else:
                     return '5 to 7'
               elif obj[9] == 'never':
                  return '<5'
               else:
                  return '<5'
            elif obj[1] == 'often':
               return '7 to 9'
            elif obj[1] == 'sometimes':
               if obj[0] == 'male':
                  return '7 to 9'
               elif obj[0] == 'female':
                  return '5 to 7'
               else:
                  return '5 to 7'
            else:
               return '5 to 7'
         elif obj[6] == '<1':
            if obj[0] == 'female':
               if obj[7] == '>4':
                  return '7 to 9'
               elif obj[7] == '1 to 4':
                  return '7 to 9'
               elif obj[7] == '<1':
                  return '5 to 7'
               else:
                  return '5 to 7'
            elif obj[0] == 'male':
               return '5 to 7'
            else:
               return '5 to 7'
         elif obj[6] == '>4':
            if obj[1] == 'never':
               return '>9'
            elif obj[1] == 'often':
               if obj[2] == 'often':
                  return '7 to 9'
               elif obj[2] == 'sometimes':
                  return '>9'
               else:
                  return '>9'
            elif obj[1] == 'sometimes':
               return '5 to 7'
            else:
               return '5 to 7'
         else:
            return '>9'
      else:
         return '5 to 7'
   elif obj[4] == 'Moderate':
      if obj[0] == 'male':
         if obj[8] == '>9':
            if obj[10]>2:
               if obj[12] == '1 to 4':
                  if obj[5] == 'often':
                     if obj[1] == 'often':
                        if obj[3] == '75 to 85':
                           return '>9'
                        elif obj[3] == '>85':
                           return '7 to 9'
                        elif obj[3] == '<75':
                           return '>9'
                        else:
                           return '>9'
                     elif obj[1] == 'sometimes':
                        if obj[3] == '>85':
                           return '<5'
                        elif obj[3] == '75 to 85':
                           return '7 to 9'
                        elif obj[3] == '<75':
                           return '<5'
                        else:
                           return '<5'
                     elif obj[1] == 'never':
                        if obj[9] == 'sometimes':
                           return '>9'
                        elif obj[9] == 'often':
                           return '7 to 9'
                        else:
                           return '7 to 9'
                     else:
                        return '>9'
                  elif obj[5] == 'sometimes':
                     if obj[6] == '>4':
                        return '5 to 7'
                     elif obj[6] == '<1':
                        if obj[3] == '>85':
                           return '7 to 9'
                        elif obj[3] == '75 to 85':
                           return '>9'
                        else:
                           return '>9'
                     elif obj[6] == '1 to 4':
                        return '7 to 9'
                     else:
                        return '7 to 9'
                  elif obj[5] == 'never':
                     if obj[11] == '>8':
                        return '5 to 7'
                     elif obj[11] == '<6':
                        return '7 to 9'
                     elif obj[11] == '6 to 8':
                        return '5 to 7'
                     else:
                        return '5 to 7'
                  else:
                     return '5 to 7'
               elif obj[12] == '<1':
                  if obj[7] == '1 to 4':
                     if obj[5] == 'often':
                        if obj[11] == '<6':
                           return '<5'
                        elif obj[11] == '6 to 8':
                           return '5 to 7'
                        else:
                           return '5 to 7'
                     elif obj[5] == 'sometimes':
                        return '>9'
                     else:
                        return '>9'
                  elif obj[7] == '>4':
                     return '>9'
                  elif obj[7] == '<1':
                     return '>9'
                  else:
                     return '>9'
               elif obj[12] == '>4':
                  if obj[7] == '1 to 4':
                     if obj[3] == '>85':
                        if obj[2] == 'sometimes':
                           if obj[5] == 'sometimes':
                              if obj[6] == '1 to 4':
                                 return '7 to 9'
                              elif obj[6] == '<1':
                                 return '<5'
                              else:
                                 return '<5'
                           elif obj[5] == 'often':
                              return '<5'
                           else:
                              return '<5'
                        elif obj[2] == 'often':
                           return '7 to 9'
                        else:
                           return '7 to 9'
                     elif obj[3] == '75 to 85':
                        return '>9'
                     elif obj[3] == '<75':
                        return '>9'
                     else:
                        return '>9'
                  elif obj[7] == '>4':
                     return '5 to 7'
                  elif obj[7] == '<1':
                     if obj[1] == 'never':
                        return '7 to 9'
                     elif obj[1] == 'sometimes':
                        return '<5'
                     else:
                        return '<5'
                  else:
                     return '<5'
               else:
                  return '>9'
            elif obj[10]<=2:
               return '>9'
            else:
               return '>9'
         elif obj[8] == '7 to 9':
            if obj[10]>2:
               if obj[12] == '1 to 4':
                  if obj[3] == '>85':
                     if obj[11] == '6 to 8':
                        if obj[7] == '1 to 4':
                           if obj[1] == 'never':
                              return '>9'
                           elif obj[1] == 'often':
                              return '>9'
                           elif obj[1] == 'sometimes':
                              return '<5'
                           else:
                              return '<5'
                        elif obj[7] == '>4':
                           return '<5'
                        else:
                           return '<5'
                     elif obj[11] == '<6':
                        if obj[7] == '1 to 4':
                           return '7 to 9'
                        elif obj[7] == '<1':
                           return '>9'
                        elif obj[7] == '>4':
                           return '5 to 7'
                        else:
                           return '5 to 7'
                     elif obj[11] == '>8':
                        if obj[2] == 'often':
                           return '5 to 7'
                        elif obj[2] == 'never':
                           return '<5'
                        else:
                           return '<5'
                     else:
                        return '<5'
                  elif obj[3] == '75 to 85':
                     if obj[2] == 'sometimes':
                        if obj[11] == '6 to 8':
                           return '>9'
                        elif obj[11] == '<6':
                           return '7 to 9'
                        elif obj[11] == '>8':
                           return '>9'
                        else:
                           return '>9'
                     elif obj[2] == 'often':
                        if obj[6] == '<1':
                           return '7 to 9'
                        elif obj[6] == '>4':
                           return '<5'
                        else:
                           return '<5'
                     elif obj[2] == 'never':
                        return '5 to 7'
                     else:
                        return '5 to 7'
                  elif obj[3] == '<75':
                     return '<5'
                  else:
                     return '<5'
               elif obj[12] == '<1':
                  if obj[11] == '<6':
                     if obj[7] == '1 to 4':
                        return '>9'
                     elif obj[7] == '<1':
                        if obj[1] == 'often':
                           return '7 to 9'
                        elif obj[1] == 'never':
                           return '>9'
                        else:
                           return '>9'
                     elif obj[7] == '>4':
                        return '<5'
                     else:
                        return '<5'
                  elif obj[11] == '6 to 8':
                     if obj[1] == 'sometimes':
                        return '>9'
                     elif obj[1] == 'often':
                        return '7 to 9'
                     elif obj[1] == 'never':
                        return '>9'
                     else:
                        return '>9'
                  elif obj[11] == '>8':
                     return '7 to 9'
                  else:
                     return '7 to 9'
               elif obj[12] == '>4':
                  if obj[11] == '6 to 8':
                     if obj[5] == 'sometimes':
                        if obj[1] == 'often':
                           return '7 to 9'
                        elif obj[1] == 'never':
                           return '>9'
                        elif obj[1] == 'sometimes':
                           return '7 to 9'
                        else:
                           return '7 to 9'
                     elif obj[5] == 'often':
                        if obj[1] == 'often':
                           return '>9'
                        elif obj[1] == 'never':
                           return '<5'
                        else:
                           return '<5'
                     elif obj[5] == 'never':
                        return '<5'
                     else:
                        return '<5'
                  elif obj[11] == '<6':
                     return '5 to 7'
                  else:
                     return '5 to 7'
               else:
                  return '<5'
            elif obj[10]<=2:
               if obj[6] == '1 to 4':
                  return '>9'
               elif obj[6] == '>4':
                  return '5 to 7'
               else:
                  return '5 to 7'
            else:
               return '>9'
         elif obj[8] == '5 to 7':
            if obj[3] == '>85':
               if obj[11] == '6 to 8':
                  if obj[6] == '1 to 4':
                     if obj[1] == 'often':
                        if obj[12] == '1 to 4':
                           return '5 to 7'
                        elif obj[12] == '<1':
                           return '>9'
                        elif obj[12] == '>4':
                           return '5 to 7'
                        else:
                           return '5 to 7'
                     elif obj[1] == 'never':
                        if obj[12] == '1 to 4':
                           return '7 to 9'
                        elif obj[12] == '<1':
                           return '5 to 7'
                        elif obj[12] == '>4':
                           return '<5'
                        else:
                           return '<5'
                     elif obj[1] == 'sometimes':
                        return '7 to 9'
                     else:
                        return '7 to 9'
                  elif obj[6] == '>4':
                     if obj[1] == 'sometimes':
                        if obj[5] == 'often':
                           return '5 to 7'
                        elif obj[5] == 'sometimes':
                           return '7 to 9'
                        else:
                           return '7 to 9'
                     elif obj[1] == 'often':
                        return '7 to 9'
                     else:
                        return '7 to 9'
                  elif obj[6] == '<1':
                     return '<5'
                  else:
                     return '<5'
               elif obj[11] == '>8':
                  if obj[12] == '1 to 4':
                     return '>9'
                  elif obj[12] == '>4':
                     return '7 to 9'
                  else:
                     return '7 to 9'
               elif obj[11] == '<6':
                  return '5 to 7'
               else:
                  return '5 to 7'
            elif obj[3] == '<75':
               if obj[5] == 'sometimes':
                  if obj[2] == 'sometimes':
                     if obj[1] == 'often':
                        if obj[6] == '1 to 4':
                           if obj[11] == '>8':
                              return '7 to 9'
                           elif obj[11] == '6 to 8':
                              return '<5'
                           else:
                              return '<5'
                        elif obj[6] == '<1':
                           return '<5'
                        else:
                           return '<5'
                     elif obj[1] == 'never':
                        return '7 to 9'
                     else:
                        return '7 to 9'
                  elif obj[2] == 'never':
                     return '7 to 9'
                  elif obj[2] == 'often':
                     if obj[6] == '<1':
                        return '<5'
                     elif obj[6] == '1 to 4':
                        return '5 to 7'
                     else:
                        return '5 to 7'
                  else:
                     return '<5'
               elif obj[5] == 'often':
                  if obj[10]>2:
                     if obj[1] == 'often':
                        return '>9'
                     elif obj[1] == 'never':
                        return '5 to 7'
                     elif obj[1] == 'sometimes':
                        return '>9'
                     else:
                        return '>9'
                  elif obj[10]<=2:
                     return '<5'
                  else:
                     return '<5'
               elif obj[5] == 'never':
                  if obj[2] == 'never':
                     return '7 to 9'
                  elif obj[2] == 'sometimes':
                     return '5 to 7'
                  else:
                     return '5 to 7'
               else:
                  return '5 to 7'
            elif obj[3] == '75 to 85':
               if obj[2] == 'never':
                  if obj[7] == '1 to 4':
                     if obj[9] == 'never':
                        return '5 to 7'
                     elif obj[9] == 'often':
                        return '<5'
                     elif obj[9] == 'sometimes':
                        return '5 to 7'
                     else:
                        return '5 to 7'
                  elif obj[7] == '<1':
                     return '<5'
                  else:
                     return '<5'
               elif obj[2] == 'sometimes':
                  return '>9'
               elif obj[2] == 'often':
                  if obj[1] == 'often':
                     return '>9'
                  elif obj[1] == 'sometimes':
                     return '<5'
                  else:
                     return '<5'
               else:
                  return '<5'
            else:
               return '>9'
         elif obj[8] == '<5':
            if obj[1] == 'sometimes':
               if obj[3] == '>85':
                  if obj[12] == '1 to 4':
                     if obj[2] == 'never':
                        return '7 to 9'
                     elif obj[2] == 'often':
                        if obj[5] == 'never':
                           return '<5'
                        elif obj[5] == 'sometimes':
                           return '7 to 9'
                        else:
                           return '7 to 9'
                     elif obj[2] == 'sometimes':
                        return '5 to 7'
                     else:
                        return '5 to 7'
                  elif obj[12] == '>4':
                     if obj[5] == 'never':
                        return '>9'
                     elif obj[5] == 'sometimes':
                        return '5 to 7'
                     else:
                        return '5 to 7'
                  elif obj[12] == '<1':
                     if obj[2] == 'often':
                        return '>9'
                     elif obj[2] == 'sometimes':
                        return '<5'
                     else:
                        return '<5'
                  else:
                     return '<5'
               elif obj[3] == '75 to 85':
                  if obj[9] == 'often':
                     return '5 to 7'
                  elif obj[9] == 'sometimes':
                     return '>9'
                  else:
                     return '>9'
               elif obj[3] == '<75':
                  return '>9'
               else:
                  return '>9'
            elif obj[1] == 'never':
               if obj[6] == '>4':
                  if obj[7] == '1 to 4':
                     return '<5'
                  elif obj[7] == '<1':
                     return '7 to 9'
                  elif obj[7] == '>4':
                     if obj[2] == 'often':
                        return '5 to 7'
                     elif obj[2] == 'sometimes':
                        return '<5'
                     else:
                        return '<5'
                  else:
                     return '<5'
               elif obj[6] == '<1':
                  if obj[9] == 'never':
                     return '7 to 9'
                  elif obj[9] == 'sometimes':
                     return '5 to 7'
                  else:
                     return '5 to 7'
               elif obj[6] == '1 to 4':
                  return '7 to 9'
               else:
                  return '7 to 9'
            elif obj[1] == 'often':
               if obj[12] == '1 to 4':
                  if obj[3] == '>85':
                     if obj[9] == 'often':
                        return '7 to 9'
                     elif obj[9] == 'never':
                        return '5 to 7'
                     elif obj[9] == 'sometimes':
                        return '5 to 7'
                     else:
                        return '5 to 7'
                  elif obj[3] == '<75':
                     return '7 to 9'
                  else:
                     return '7 to 9'
               elif obj[12] == '<1':
                  if obj[3] == '75 to 85':
                     return '5 to 7'
                  elif obj[3] == '<75':
                     return '7 to 9'
                  else:
                     return '7 to 9'
               elif obj[12] == '>4':
                  if obj[2] == 'never':
                     if obj[3] == '75 to 85':
                        return '7 to 9'
                     elif obj[3] == '<75':
                        return '>9'
                     else:
                        return '>9'
                  elif obj[2] == 'sometimes':
                     return '>9'
                  else:
                     return '>9'
               else:
                  return '>9'
            else:
               return '5 to 7'
         else:
            return '7 to 9'
      elif obj[0] == 'female':
         if obj[11] == '6 to 8':
            if obj[10]>2:
               if obj[6] == '1 to 4':
                  if obj[3] == '<75':
                     if obj[5] == 'sometimes':
                        if obj[2] == 'never':
                           if obj[1] == 'never':
                              if obj[9] == 'never':
                                 return '>9'
                              elif obj[9] == 'often':
                                 return '7 to 9'
                              else:
                                 return '7 to 9'
                           elif obj[1] == 'often':
                              return '7 to 9'
                           elif obj[1] == 'sometimes':
                              return '7 to 9'
                           else:
                              return '7 to 9'
                        elif obj[2] == 'often':
                           if obj[9] == 'never':
                              if obj[8] == '<5':
                                 return '5 to 7'
                              elif obj[8] == '5 to 7':
                                 return '5 to 7'
                              elif obj[8] == '>9':
                                 return '7 to 9'
                              else:
                                 return '7 to 9'
                           elif obj[9] == 'often':
                              return '<5'
                           elif obj[9] == 'sometimes':
                              return '7 to 9'
                           else:
                              return '7 to 9'
                        elif obj[2] == 'sometimes':
                           if obj[7] == '<1':
                              return '7 to 9'
                           elif obj[7] == '1 to 4':
                              return '>9'
                           else:
                              return '>9'
                        else:
                           return '7 to 9'
                     elif obj[5] == 'often':
                        return '>9'
                     else:
                        return '>9'
                  elif obj[3] == '75 to 85':
                     if obj[5] == 'sometimes':
                        if obj[1] == 'often':
                           if obj[9] == 'sometimes':
                              return '>9'
                           elif obj[9] == 'often':
                              return '5 to 7'
                           else:
                              return '5 to 7'
                        elif obj[1] == 'never':
                           return '5 to 7'
                        else:
                           return '5 to 7'
                     elif obj[5] == 'never':
                        if obj[12] == '1 to 4':
                           return '5 to 7'
                        elif obj[12] == '<1':
                           return '<5'
                        else:
                           return '<5'
                     elif obj[5] == 'often':
                        return '<5'
                     else:
                        return '<5'
                  elif obj[3] == '>85':
                     if obj[8] == '7 to 9':
                        if obj[2] == 'often':
                           return '<5'
                        elif obj[2] == 'never':
                           return '7 to 9'
                        elif obj[2] == 'sometimes':
                           return '7 to 9'
                        else:
                           return '7 to 9'
                     elif obj[8] == '5 to 7':
                        return '>9'
                     elif obj[8] == '>9':
                        return '<5'
                     else:
                        return '<5'
                  else:
                     return '<5'
               elif obj[6] == '<1':
                  if obj[8] == '>9':
                     if obj[5] == 'often':
                        if obj[3] == '>85':
                           return '5 to 7'
                        elif obj[3] == '<75':
                           return '7 to 9'
                        else:
                           return '7 to 9'
                     elif obj[5] == 'sometimes':
                        return '>9'
                     elif obj[5] == 'never':
                        return '7 to 9'
                     else:
                        return '7 to 9'
                  elif obj[8] == '<5':
                     if obj[1] == 'never':
                        return '5 to 7'
                     elif obj[1] == 'sometimes':
                        return '5 to 7'
                     elif obj[1] == 'often':
                        return '7 to 9'
                     else:
                        return '7 to 9'
                  elif obj[8] == '5 to 7':
                     if obj[2] == 'never':
                        return '7 to 9'
                     elif obj[2] == 'often':
                        return '5 to 7'
                     elif obj[2] == 'sometimes':
                        return '5 to 7'
                     else:
                        return '5 to 7'
                  elif obj[8] == '7 to 9':
                     if obj[3] == '>85':
                        return '7 to 9'
                     elif obj[3] == '75 to 85':
                        return '>9'
                     elif obj[3] == '<75':
                        return '7 to 9'
                     else:
                        return '7 to 9'
                  else:
                     return '7 to 9'
               elif obj[6] == '>4':
                  if obj[9] == 'often':
                     if obj[8] == '5 to 7':
                        if obj[3] == '75 to 85':
                           return '7 to 9'
                        elif obj[3] == '>85':
                           return '7 to 9'
                        elif obj[3] == '<75':
                           return '5 to 7'
                        else:
                           return '5 to 7'
                     elif obj[8] == '<5':
                        if obj[5] == 'never':
                           return '>9'
                        elif obj[5] == 'sometimes':
                           return '7 to 9'
                        else:
                           return '7 to 9'
                     elif obj[8] == '>9':
                        return '5 to 7'
                     else:
                        return '5 to 7'
                  elif obj[9] == 'never':
                     if obj[1] == 'often':
                        return '5 to 7'
                     elif obj[1] == 'never':
                        return '5 to 7'
                     elif obj[1] == 'sometimes':
                        if obj[2] == 'often':
                           return '>9'
                        elif obj[2] == 'never':
                           return '7 to 9'
                        else:
                           return '7 to 9'
                     else:
                        return '7 to 9'
                  elif obj[9] == 'sometimes':
                     return '5 to 7'
                  else:
                     return '5 to 7'
               else:
                  return '5 to 7'
            elif obj[10]<=2:
               if obj[5] == 'sometimes':
                  if obj[1] == 'often':
                     if obj[3] == '>85':
                        return '<5'
                     elif obj[3] == '75 to 85':
                        return '7 to 9'
                     elif obj[3] == '<75':
                        return '<5'
                     else:
                        return '<5'
                  elif obj[1] == 'never':
                     return '7 to 9'
                  else:
                     return '7 to 9'
               elif obj[5] == 'often':
                  return '5 to 7'
               else:
                  return '5 to 7'
            else:
               return '<5'
         elif obj[11] == '>8':
            if obj[5] == 'sometimes':
               if obj[9] == 'sometimes':
                  if obj[12] == '1 to 4':
                     if obj[2] == 'never':
                        return '5 to 7'
                     elif obj[2] == 'often':
                        return '7 to 9'
                     elif obj[2] == 'sometimes':
                        return '>9'
                     else:
                        return '>9'
                  elif obj[12] == '<1':
                     if obj[6] == '<1':
                        return '5 to 7'
                     elif obj[6] == '1 to 4':
                        return '7 to 9'
                     else:
                        return '7 to 9'
                  elif obj[12] == '>4':
                     if obj[3] == '>85':
                        return '<5'
                     elif obj[3] == '<75':
                        return '7 to 9'
                     else:
                        return '7 to 9'
                  else:
                     return '<5'
               elif obj[9] == 'often':
                  if obj[12] == '1 to 4':
                     if obj[3] == '<75':
                        return '7 to 9'
                     elif obj[3] == '>85':
                        return '7 to 9'
                     elif obj[3] == '75 to 85':
                        return '5 to 7'
                     else:
                        return '5 to 7'
                  elif obj[12] == '<1':
                     return '7 to 9'
                  elif obj[12] == '>4':
                     return '5 to 7'
                  else:
                     return '5 to 7'
               elif obj[9] == 'never':
                  return '5 to 7'
               else:
                  return '5 to 7'
            elif obj[5] == 'never':
               if obj[3] == '>85':
                  if obj[12] == '1 to 4':
                     if obj[8] == '<5':
                        return '7 to 9'
                     elif obj[8] == '5 to 7':
                        return '5 to 7'
                     elif obj[8] == '7 to 9':
                        return '7 to 9'
                     elif obj[8] == '>9':
                        return '5 to 7'
                     else:
                        return '5 to 7'
                  elif obj[12] == '<1':
                     return '>9'
                  else:
                     return '>9'
               elif obj[3] == '75 to 85':
                  return '>9'
               elif obj[3] == '<75':
                  if obj[1] == 'never':
                     return '7 to 9'
                  elif obj[1] == 'sometimes':
                     return '>9'
                  else:
                     return '>9'
               else:
                  return '7 to 9'
            elif obj[5] == 'often':
               if obj[1] == 'often':
                  if obj[3] == '>85':
                     if obj[8] == '7 to 9':
                        return '7 to 9'
                     elif obj[8] == '>9':
                        return '<5'
                     else:
                        return '<5'
                  elif obj[3] == '<75':
                     return '<5'
                  else:
                     return '<5'
               elif obj[1] == 'never':
                  if obj[3] == '>85':
                     return '>9'
                  elif obj[3] == '75 to 85':
                     return '5 to 7'
                  else:
                     return '5 to 7'
               elif obj[1] == 'sometimes':
                  if obj[3] == '75 to 85':
                     return '>9'
                  elif obj[3] == '>85':
                     return '7 to 9'
                  else:
                     return '7 to 9'
               else:
                  return '7 to 9'
            else:
               return '7 to 9'
         elif obj[11] == '<6':
            if obj[10]>2:
               if obj[7] == '>4':
                  if obj[9] == 'never':
                     if obj[6] == '<1':
                        if obj[1] == 'often':
                           if obj[12] == '1 to 4':
                              return '>9'
                           elif obj[12] == '>4':
                              return '7 to 9'
                           else:
                              return '7 to 9'
                        elif obj[1] == 'never':
                           return '7 to 9'
                        else:
                           return '7 to 9'
                     elif obj[6] == '1 to 4':
                        if obj[8] == '<5':
                           return '>9'
                        elif obj[8] == '5 to 7':
                           return '5 to 7'
                        else:
                           return '5 to 7'
                     elif obj[6] == '>4':
                        return '5 to 7'
                     else:
                        return '5 to 7'
                  elif obj[9] == 'sometimes':
                     if obj[8] == '<5':
                        return '<5'
                     elif obj[8] == '5 to 7':
                        return '7 to 9'
                     elif obj[8] == '7 to 9':
                        return '5 to 7'
                     elif obj[8] == '>9':
                        return '7 to 9'
                     else:
                        return '7 to 9'
                  elif obj[9] == 'often':
                     if obj[2] == 'often':
                        return '>9'
                     elif obj[2] == 'never':
                        return '5 to 7'
                     else:
                        return '5 to 7'
                  else:
                     return '>9'
               elif obj[7] == '<1':
                  if obj[9] == 'never':
                     if obj[3] == '<75':
                        if obj[2] == 'never':
                           return '>9'
                        elif obj[2] == 'often':
                           return '5 to 7'
                        elif obj[2] == 'sometimes':
                           return '>9'
                        else:
                           return '>9'
                     elif obj[3] == '>85':
                        return '5 to 7'
                     else:
                        return '5 to 7'
                  elif obj[9] == 'often':
                     if obj[5] == 'often':
                        return '7 to 9'
                     elif obj[5] == 'sometimes':
                        return '<5'
                     elif obj[5] == 'never':
                        return '<5'
                     else:
                        return '<5'
                  elif obj[9] == 'sometimes':
                     if obj[1] == 'often':
                        return '>9'
                     elif obj[1] == 'never':
                        return '5 to 7'
                     elif obj[1] == 'sometimes':
                        return '7 to 9'
                     else:
                        return '7 to 9'
                  else:
                     return '5 to 7'
               elif obj[7] == '1 to 4':
                  if obj[12] == '<1':
                     if obj[2] == 'often':
                        return '<5'
                     elif obj[2] == 'sometimes':
                        if obj[1] == 'never':
                           return '>9'
                        elif obj[1] == 'sometimes':
                           return '<5'
                        else:
                           return '<5'
                     else:
                        return '<5'
                  elif obj[12] == '1 to 4':
                     if obj[6] == '1 to 4':
                        return '>9'
                     elif obj[6] == '<1':
                        return '7 to 9'
                     else:
                        return '7 to 9'
                  elif obj[12] == '>4':
                     if obj[2] == 'often':
                        return '>9'
                     elif obj[2] == 'never':
                        return '7 to 9'
                     elif obj[2] == 'sometimes':
                        return '>9'
                     else:
                        return '>9'
                  else:
                     return '>9'
               else:
                  return '>9'
            elif obj[10]<=2:
               if obj[1] == 'often':
                  return '7 to 9'
               elif obj[1] == 'sometimes':
                  return '>9'
               else:
                  return '>9'
            else:
               return '7 to 9'
         else:
            return '>9'
      else:
         return '7 to 9'
   else:
      return '7 to 9'
