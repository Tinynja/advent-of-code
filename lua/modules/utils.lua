if utils then io.write("Reloaded utils.lua.\n") end
utils = true

function toboolean(v)
	if type(v) == "boolean" then
		return v
	elseif type(v) == "number" then
		if v == 1 then return true end
	elseif type(v) == "string" then
		if v == "true" then return true end
	end
	return false
end

if _tostring == nil then _tostring = tostring end
function tostring(...)
	local args = {table.unpack({...})}
	local strings = {_tostring(args[1])}
	for i = 2,#args do
		table.insert(strings,_tostring(args[i]))
	end
	return table.unpack(strings)
end

if _tonumber == nil then _tonumber = tonumber end
function tonumber(n,b)
	local nums = {}
	if type(n) == 'table' then
		for k,v in pairs(n) do
			table.insert(nums,tonumber(v,b))
		end
	else
		table.insert(nums,_tonumber(n,b))
	end
	return table.unpack(nums)
end

function math.sum(...)
	local args,sum = {...},0
	for i = 1,#args do
		print(type(args[i]))
		if type(args[i]) == 'table' then
			sum = sum+math.sum(args[i])
		elseif type(args[i]) == 'number' then
			sum = sum+args[i]
		else
			error("bad argument #"..i.." to 'sum' (number expected, got "..type(args[i])..")")
		end
	end
	return sum
end

if string._byte == nil then string._byte = string.byte end
function string.byte(s,i,j)
	local ascii = {string._byte(s,i,j)}
	if ascii[1] == nil then
		return -1
	end
	return table.unpack(ascii)
end
 
function string.cut(s,pattern,delpattern,i)
  if type(s) ~= "string" then error("bad argument #1 to 'string.cut' (string expected, got "..type(t)..")") end
  if type(pattern) ~= "string" then error("bad argument #2 to 'string.cut' (string expected, got "..type(t)..")") end
	local i3 = 0
	if delpattern == nil then delpattern = true end
	if tonumber(i) ~= nil then i2 = i-1 end
	local cutstring = {}
	repeat
		local i1 = i3
    i2,i3 = s:find(pattern,i1+1)
		if i2 == nil then i2 = s:len()+1 end
		if delpattern then
			table.insert(cutstring,s:sub(i1+1,i2-1))
		else
			table.insert(cutstring,s:sub(i1,i2-1))
		end
	until i2 == s:len()+1
  return cutstring
end

function alphabetical(s1,s2,returnstring) --need to add ability to sort negative numbers
  if not (type(s1) == "string" or type(s1) == "number") then error("bad argument #1 to 'alphabetical' (string expected, got "..type(s1)..")") end
	if not (type(s2) == "string" or type(s2) == "number") then error("bad argument #2 to 'alphabetical' (string expected, got "..type(s2)..")") end
	local t,f = 0,0 -- true,false
	if returnstring then t,f = s1,s2
	else t,f = true,false
	end
	if not tostring(s1) and not tostring(s2) then return f
	elseif not tostring(s2) then return t
	elseif not tostring(s1) then return f
	else s1,s2 = tostring(s1,s2)
	end
	local low1,low2 = s1:lower(),s2:lower()
	for i = 1,math.max(s1:len(),s2:len()) do
		local l1,l2 = low1:byte(i,i),low2:byte(i,i)
		local r1,r2 = s1:byte(i,i),s2:byte(i,i)
		if tonumber(low1:sub(i,i)) ~= nil and tonumber(low2:sub(i,i)) ~= nil then
			l1,l2 = tonumber(low1:match("%d+",i),low2:match("%d+",i))
			i = math.max(low1:find("%d+"),low2:find("%d+"))
		end
		if l1 < l2 or r1 < r2 then return t
		elseif l2 < l1 or r2 < r1 then return f
		elseif i == low2:len() then return f
		elseif i == low1:len() then return t
		end
	end
end

function copy(orig)
	local clone = {}
	if type(orig) == 'table' then
		for k,v in pairs(orig) do
			clone[k] = copy(v)
		end
		setmetatable(clone, copy(getmetatable(orig)))
	else
		clone = orig
	end
	return clone
end

function backspace(n)
	io.write(string.rep('\008',n))
	io.write(string.rep(' ',n))
	io.write(string.rep('\008',n))
end

function table.shift(t,n)
	local indexes,sign = {},(n/math.abs(n))
	for k,v in pairs(t) do
		if tonumber(k) ~= nil then
			table.insert(indexes,k)
		end
	end
	-- if n > 0 then for 1,#indexes; elseif n < 0 then for #indexes,1,-1
	if #indexes > 0 then
		for i = math.max(1,sign*(#indexes)),math.max(1,-sign*(#indexes)),-sign do
			t[i+n] = t[i]
			t[i] = nil
		end
	end
	return t
end

-- Returns all the indexes where "value" can be found. "kv" is for precising
-- if search should be done within the keys or within the values. To get all
-- index inside a table one should use indexes = {table.find(t,value,kv)}
function table.find(t,value,kv)
  if type(t) ~= "table" then error("bad argument #1 to 'table.find' (table expected, got "..type(t)..")") end
	if type(value) == nil then error("bad argument #2 to 'table.find' (value expected, got "..type(value)..")") end
	if kv == nil or not kv:match('[kv]') then
		kv = 'v'
	end
	local indexes = {}
	for k,v in pairs(t) do
		if type(v) == 'table' then
			local suffixes = {table.find(v,value,kv)}
			if suffixes[1] then
				for i = 1,#suffixes do
					table.insert(indexes,k..'.'..suffixes[i])
				end
			end
		elseif (kv:match('k') and k == value) or (kv:match('v') and v == value) then
			table.insert(indexes,k)
		end
	end
	if next(indexes) ~= nil then
		return table.unpack(indexes)
	end
	return false
end

function sleep(n)  -- seconds
	local start = os.clock()
  while os.clock()-start <= n do end
end

function orderedPairs(t)
	return orderedNext, t, "__nil"
end

function orderedNext(t,state)
	if t.__orderedIndex == nil then
		local indexes = {[0] = "__nil"}
		for k in pairs(t) do
			table.insert(indexes,k)
		end
		table.sort(indexes,alphabetical)
		t.__orderedIndex = indexes
	end
	local i = table.find(t.__orderedIndex,state)+1
	if i > #t.__orderedIndex then
		t.__orderedIndex = nil
		return nil
	else
		return t.__orderedIndex[i], t[t.__orderedIndex[i]]
	end
end