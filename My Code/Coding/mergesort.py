def merge_sort(a):
  if len(a) < 2:
    return a
  mitte = len(a) // 2
  l = merge_sort(a[:mitte])
  r = merge_sort(a[mitte:])
  return verschmelze(l, r)
  r = merge_sort(a[mitte:])
  return verschmelze(l, r)

def verschmelze(l, r):
  indexergebnis = []
  indexl = indexr = 0
  while indexl < len(l) and indexr < len(r):
    if left[indexl] < right[indexr]:
      indexergebnis.append(l[indexl])
      indexl += 1
    else:
      indexergebnis.append(r[indexr])
      indexr += 1
    indexergebnis += l[indexl:]
    indexergebnis += r[indexr:]
    return indexergebnis